#define MyAppName "Photo Enhancement Studio"
#define MyAppVersion "0.1.0"
[Setup]
AppId={{3B99A3E1-6E25-49B8-B39E-86AA41F5B172}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\Photo Enhancement Studio
DefaultGroupName={#MyAppName}
OutputDir=installer-output
OutputBaseFilename=Photo_Enhancement_Studio_Setup_0.1.0
Compression=lzma
SolidCompression=yes
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
[Files]
Source: "dist\PhotoEnhancementStudio\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion
[Icons]
Name: "{group}\Photo Enhancement Studio"; Filename: "{app}\PhotoEnhancementStudio.exe"
Name: "{autodesktop}\Photo Enhancement Studio"; Filename: "{app}\PhotoEnhancementStudio.exe"; Tasks: desktopicon
[Tasks]
Name: desktopicon; Description: "Create desktop shortcut"; Flags: unchecked
[Run]
Filename: "{app}\PhotoEnhancementStudio.exe"; Description: "Launch Photo Enhancement Studio"; Flags: nowait postinstall skipifsilent
