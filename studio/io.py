"""Import individual files, folders and ZIPs without path traversal."""
from pathlib import Path
import zipfile
from PIL import Image
EXTENSIONS = {'.jpg', '.jpeg', '.png', '.tif', '.tiff', '.bmp', '.webp'}
MAX_FILES = 5000
MAX_TOTAL_UNCOMPRESSED = 4 * 1024**3

def collect(paths, extraction_root: Path):
    extraction_root.mkdir(parents=True, exist_ok=True)
    results = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            results.extend(p for p in sorted(path.rglob('*')) if p.suffix.lower() in EXTENSIONS and p.is_file())
        elif path.suffix.lower() == '.zip':
            with zipfile.ZipFile(path) as archive:
                infos = [i for i in archive.infolist() if not i.is_dir() and Path(i.filename).suffix.lower() in EXTENSIONS]
                if len(infos) > MAX_FILES or sum(i.file_size for i in infos) > MAX_TOTAL_UNCOMPRESSED:
                    raise ValueError('ZIP exceeds safe import limits')
                folder = extraction_root / f'archive_{len(results)}'
                folder.mkdir(parents=True, exist_ok=True)
                for idx, info in enumerate(infos):
                    # Unique generated names avoid traversal and collisions.
                    target = folder / f'{idx:05d}_{Path(info.filename).name}'
                    with archive.open(info) as src, target.open('wb') as dst:
                        import shutil
                        shutil.copyfileobj(src, dst)
                    results.append(target)
        elif path.suffix.lower() in EXTENSIONS and path.is_file():
            results.append(path)
    if len(results) > MAX_FILES:
        raise ValueError('Too many photographs in one import')
    valid = []
    for p in results:
        try:
            with Image.open(p) as im:
                im.verify()
            valid.append(p)
        except Exception:
            continue
    return valid
