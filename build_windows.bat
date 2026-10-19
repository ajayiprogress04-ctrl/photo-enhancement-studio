@echo off
setlocal
py -m pip install -r requirements.txt
if errorlevel 1 exit /b 1
py -m PyInstaller --noconfirm --clean --windowed --onedir --name "PhotoEnhancementStudio" main.py
if errorlevel 1 exit /b 1
echo Build created in dist\PhotoEnhancementStudio\
echo To produce a setup EXE, install Inno Setup 6 and compile installer.iss
