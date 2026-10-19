"""Conservative, non-generative photographic enhancement."""
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageStat
import numpy as np

def enhance(source: Image.Image, strength: float = 0.65) -> Image.Image:
    """Return enhanced RGB image; never synthesize/reconstruct facial content."""
    if not 0 <= strength <= 1:
        raise ValueError('strength must be between 0 and 1')
    im = ImageOps.exif_transpose(source).convert('RGB')
    # Estimate neutral white balance from non-saturated, mid-tone pixels.
    arr = np.asarray(im, dtype=np.float32)
    lum = arr.mean(axis=2)
    mask = (lum > 35) & (lum < 215) & (arr.max(axis=2) < 245)
    if np.count_nonzero(mask) > 100:
        means = arr[mask].mean(axis=0)
        target = float(means.mean())
        gains = np.clip(target / np.maximum(means, 1), .92, 1.08)
        gains = 1 + (gains - 1) * strength
        arr = np.clip(arr * gains[None, None, :], 0, 255)
    im = Image.fromarray(arr.astype('uint8'), 'RGB')
    gray = ImageStat.Stat(im.convert('L'))
    mean, std = gray.mean[0], gray.stddev[0]
    if mean < 105:
        im = ImageEnhance.Brightness(im).enhance(1 + min(.15, (105-mean)/300) * strength)
    elif mean > 180:
        im = ImageEnhance.Brightness(im).enhance(1 - min(.10, (mean-180)/350) * strength)
    if std < 48:
        im = ImageEnhance.Contrast(im).enhance(1 + .12 * strength)
    im = ImageEnhance.Color(im).enhance(1 + .055 * strength)
    # Modest unsharp mask; avoids hallucinated texture or facial reconstruction.
    if strength > 0:
        im = im.filter(ImageFilter.UnsharpMask(radius=1.1, percent=int(45 * strength), threshold=4))
    return im

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
