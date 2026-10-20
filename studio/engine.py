"""Offline, non-generative photographic corrections. No face synthesis."""
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np

PRESETS = ('Natural Professional', 'Premium Camera Look', 'Cinematic Professional')

def enhance(source: Image.Image, strength: float = 0.65, preset: str = 'Premium Camera Look') -> Image.Image:
    """Apply scene-adaptive tonal and color adjustments, retaining image geometry."""
    if not 0 <= strength <= 1:
        raise ValueError('strength must be between 0 and 1')
    if preset not in PRESETS:
        raise ValueError(f'Unknown preset: {preset}')
    im = ImageOps.exif_transpose(source).convert('RGB')
    if strength == 0:
        return im.copy()
    a = np.asarray(im, dtype=np.float32) / 255.0
    # Robust, conservative channel balancing: prevent strongly colored scenes
    # from being aggressively neutralized.
    luminance = a @ np.array([.2126, .7152, .0722], dtype=np.float32)
    valid = (luminance > .13) & (luminance < .88) & (a.max(axis=2) < .96)
    if valid.sum() > 100:
        means = a[valid].mean(axis=0)
        gains = np.clip(means.mean() / np.maximum(means, .02), .93, 1.07)
        a *= (1 + (gains - 1) * strength)[None, None, :]
    a = np.clip(a, 0, 1)
    # Smooth shadow lift and highlight roll-off. Retain clipped areas as clipped;
    # no synthetic detail recovery is claimed.
    lum = np.clip(a @ np.array([.2126, .7152, .0722], dtype=np.float32), 0, 1)
    mid = float(np.median(lum))
    exposure = np.clip((.46 - mid) * .48, -.10, .13) * strength
    shadow = (1 - lum) ** 2
    highlight = lum ** 3
    lift = (.095 + max(0, exposure)) * strength * shadow
    compress = (.055 + max(0, -exposure)) * strength * highlight
    target = np.clip(lum + lift - compress + exposure * .35, 0, 1)
    a = np.clip(a * ((target + .015) / (lum + .015))[..., None], 0, 1)
    # Mild contrast curve and restrained saturation, depending on aesthetic.
    contrast, saturation, sharpen = {
        'Natural Professional': (.075, .035, .50),
        'Premium Camera Look': (.13, .075, .75),
        'Cinematic Professional': (.16, .055, .65),
    }[preset]
    a = np.clip((a - .5) * (1 + contrast * strength) + .5, 0, 1)
    gray = (a @ np.array([.2126, .7152, .0722], dtype=np.float32))[..., None]
    a = np.clip(gray + (a - gray) * (1 + saturation * strength), 0, 1)
    if preset == 'Cinematic Professional':
        # Subtle cool shadows / warm highlights, not a scene replacement.
        weight = np.clip(gray * 2 - .5, 0, 1)
        tint = np.array([.012, .002, -.012], dtype=np.float32) * weight + np.array([-.008, .002, .012], dtype=np.float32) * (1-weight)
        a = np.clip(a + tint * strength, 0, 1)
    result = Image.fromarray(np.round(a * 255).astype('uint8'), 'RGB')
    # Only suppress visible high-frequency noise when measurable; avoid blur on
    # smooth clean photos. This is not AI denoising or deblurring.
    sample = np.asarray(result.convert('L').resize((min(result.width, 512), min(result.height, 512))), dtype=np.float32)
    if min(sample.shape) >= 12:
        residual = sample[1:-1,1:-1] - (sample[:-2,1:-1]+sample[2:,1:-1]+sample[1:-1,:-2]+sample[1:-1,2:])*.25
        noisy = float(np.median(np.abs(residual))) > 5.5
        if noisy and strength >= .35:
            filtered = result.filter(ImageFilter.MedianFilter(size=3))
            result = Image.blend(result, filtered, .10 * strength)
    if min(result.size) > 24:
        result = result.filter(ImageFilter.UnsharpMask(radius=1.15, percent=int(90 * sharpen * strength), threshold=4))
    return result

def save_image(image: Image.Image, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    suffix = destination.suffix.lower()
    if suffix in ('.jpg', '.jpeg'):
        image.save(destination, 'JPEG', quality=95, subsampling=0)
    elif suffix == '.png':
        image.save(destination, 'PNG', optimize=True)
    elif suffix in ('.tif', '.tiff'):
        image.save(destination, 'TIFF', compression='tiff_lzw')
    else:
        raise ValueError(f'Unsupported export format: {suffix}')
