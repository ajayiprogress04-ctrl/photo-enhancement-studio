# Professional Photo Enhancement Studio — Windows prototype v0.1.0

A **fully offline, non-generative** photo-enhancement desktop prototype, using your supplied App Design Preferences as a visual guide. No cloud accounts or API keys.

## What works in this version
- Import JPEG/PNG/TIFF/BMP/WebP files, folders and ZIP archives.
- Image-by-image adaptive white-balance, mild exposure, contrast, color and sharpening adjustments.
- Side-by-side original/enhanced previews and strength slider.
- Batch export as JPEG files to a folder or a single ZIP.
- Light, Dark and Colour themes; chosen theme persists locally.
- Original image files are never overwritten by the editor.

## Run on Windows
1. Install Python 3.11 or 3.12 (64-bit) from python.org and select **Add Python to PATH**.
2. Extract this entire project ZIP.
3. Open Command Prompt in the extracted folder.
4. Run `py -m pip install -r requirements.txt`.
5. Run `py main.py`.

## Create a Windows desktop build and setup installer
1. On **Windows**, double-click `build_windows.bat` to create `dist\PhotoEnhancementStudio\`.
2. Install **Inno Setup 6** on your build PC.
3. Open `installer.iss` in Inno Setup and click **Compile**.
4. Find the offline installer in `installer-output\Photo_Enhancement_Studio_Setup_0.1.0.exe`.
5. Test it on a clean Windows 10/11 machine with no Python installed before distributing.

Note: The project ZIP is source code, **not** a precompiled Windows installer. Build tools are needed on the build PC only.

## Important limitations
- This prototype does **not** implement AI denoising, face segmentation, RAW processing, deblurring, highlight reconstruction, color-managed ICC workflows, or facial identity verification.
- Its algorithm does not intentionally regenerate features, but **identity preservation is not formally certified**.
- JPEG exports are lossy and may discard original metadata. The preview is downsampled for speed; export processes full image dimensions.
- ZIP imports are limited by count and declared uncompressed size; maliciously malformed archives may require further safeguards.
- Preview adjustment on large images and extensive imports may briefly occupy the UI; export is threaded.
- This has not yet been tested on Windows or built into a real setup EXE.

## Project files
- `main.py`: Qt desktop interface and batch export worker
- `studio/engine.py`: conservative enhancement pipeline
- `studio/io.py`: imports and ZIP handling
- `tests/test_engine.py`: basic enhancement checks
- `build_windows.bat`: Windows PyInstaller build
- `installer.iss`: Inno Setup recipe
- `App_Preferences.md`: supplied design brief
- `Image_Enhancement_Requirements.txt`: supplied image processing requirements

## Design adaptations
Light/Dark/Colour themes use deep burgundy accents and compact layouts. The desktop uses Qt controls rather than the web reference's CSS; preferred fonts are used when installed and fall back to system fonts. Educational-only rules and website sharing controls are intentionally excluded.
