"""Photo Enhancement Studio - offline Windows desktop prototype."""
import json
import sys
import tempfile
import zipfile
from pathlib import Path
from PIL import Image
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QListWidget, QFileDialog, QComboBox, QSlider, QProgressBar,
    QSplitter, QMessageBox, QCheckBox)
from studio.engine import enhance, save_image
from studio.io import collect

CONFIG = Path.home() / '.photo_enhancement_studio.json'
PALETTES = {
 'Light': ('#f4eee8','#ffffff','#201b26','#791c40','#d4c5b5'),
 'Dark': ('#0c0c12','#1a1921','#f5f1ed','#aa456b','#44404c'),
 'Colour': ('#25101f','#3b1930','#fff4eb','#c05a79','#735062'),
}
class BatchWorker(QThread):
    progress = Signal(int, str)
    completed = Signal(str)
    failed = Signal(str)
    def __init__(self, paths, destination, strength, as_zip):
        super().__init__(); self.paths=paths; self.destination=Path(destination); self.strength=strength; self.as_zip=as_zip
    def run(self):
        try:
            folder = self.destination if not self.as_zip else Path(tempfile.mkdtemp(prefix='pes_export_'))
            folder.mkdir(parents=True, exist_ok=True)
            used = set()
            for idx, path in enumerate(self.paths):
                with Image.open(path) as src:
                    edited = enhance(src, self.strength)
                stem = path.stem
                name = f'{stem}_enhanced.jpg'
                if name.lower() in used:
                    name = f'{stem}_{idx:04d}_enhanced.jpg'
                used.add(name.lower())
                save_image(edited, folder/name)
                self.progress.emit(int((idx+1)*100/len(self.paths)), path.name)
            if self.as_zip:
                with zipfile.ZipFile(self.destination, 'w', zipfile.ZIP_DEFLATED) as z:
                    for p in folder.glob('*.jpg'): z.write(p, p.name)
                import shutil
                shutil.rmtree(folder, ignore_errors=True)
            self.completed.emit(str(self.destination))
        except Exception as exc:
            self.failed.emit(str(exc))

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Professional Photo Enhancement Studio')
        self.resize(1150, 750)
        self.paths=[]
        self.temp=tempfile.TemporaryDirectory(prefix='pes_import_')
        try: self.settings=json.loads(CONFIG.read_text(encoding='utf-8'))
        except Exception: self.settings={}
        root=QWidget(); self.setCentralWidget(root)
        main=QVBoxLayout(root)
        title=QLabel('Photo Enhancement Studio'); title.setObjectName('title'); main.addWidget(title)
        subtitle=QLabel('Professional, natural photographic correction · Fully offline'); main.addWidget(subtitle)
        toolbar=QHBoxLayout(); main.addLayout(toolbar)
        for label, action in [('Add photos / ZIP', self.add_files), ('Add folder', self.add_folder), ('Export enhanced', self.export)]:
            btn=QPushButton(label); btn.clicked.connect(action); toolbar.addWidget(btn)
        toolbar.addStretch()
        toolbar.addWidget(QLabel('Theme'))
        self.theme=QComboBox(); self.theme.addItems(PALETTES); self.theme.setCurrentText(self.settings.get('theme','Light'))
        self.theme.currentTextChanged.connect(self.apply_theme); toolbar.addWidget(self.theme)
        split=QSplitter(); main.addWidget(split,1)
        left=QWidget(); left_layout=QVBoxLayout(left); left_layout.addWidget(QLabel('Imported photographs'))
        self.items=QListWidget(); self.items.currentRowChanged.connect(self.preview); left_layout.addWidget(self.items)
        split.addWidget(left)
        right=QWidget(); right_layout=QVBoxLayout(right)
        previews=QHBoxLayout(); right_layout.addLayout(previews,1)
        self.original=QLabel('Import a photograph to begin'); self.edited=QLabel('Enhanced preview')
        for heading, widget in [('Original',self.original),('Enhanced',self.edited)]:
            column=QVBoxLayout(); column.addWidget(QLabel(heading)); widget.setAlignment(Qt.AlignCenter)
            widget.setMinimumSize(250,260); widget.setStyleSheet('border: 1px solid #777777; border-radius: 7px;')
            column.addWidget(widget,1); previews.addLayout(column,1)
        right_layout.addWidget(QLabel('Enhancement strength'))
        self.strength=QSlider(Qt.Horizontal); self.strength.setRange(0,100); self.strength.setValue(65)
        self.strength.valueChanged.connect(self.preview_current); right_layout.addWidget(self.strength)
        self.progress=QProgressBar(); right_layout.addWidget(self.progress)
        self.status=QLabel('Ready. Original files are never overwritten.'); right_layout.addWidget(self.status)
        split.addWidget(right); split.setSizes([260,850])
        self.apply_theme(self.theme.currentText())
    def apply_theme(self, name):
        bg,surface,fg,accent,border=PALETTES[name]
        self.setStyleSheet(f'''QMainWindow,QWidget{{background:{bg};color:{fg};font-family:"Source Sans 3","Segoe UI";font-size:12px;}}
          QLabel#title{{font-family:"Cormorant Garamond",Georgia;font-size:30px;font-weight:bold;}}
          QPushButton{{background:{accent};color:#ffffff;padding:9px 14px;border-radius:6px;font-weight:600;}}
          QPushButton:disabled{{background:{border};}} QPushButton:focus,QComboBox:focus,QListWidget:focus{{border:2px solid {accent};}}
          QListWidget,QComboBox{{background:{surface};color:{fg};border:1px solid {border};border-radius:6px;padding:5px;}}
          QProgressBar{{border:1px solid {border};border-radius:5px;text-align:center;}}
          QProgressBar::chunk{{background:{accent};}}''')
        CONFIG.write_text(json.dumps({'theme':name}),encoding='utf-8')
    def add_files(self):
        files,_=QFileDialog.getOpenFileNames(self,'Import photographs or ZIP','','Images and archives (*.jpg *.jpeg *.png *.tif *.tiff *.bmp *.webp *.zip)')
        if files: self.import_paths(files)
    def add_folder(self):
        folder=QFileDialog.getExistingDirectory(self,'Choose photo folder')
        if folder: self.import_paths([folder])
    def import_paths(self, paths):
        try:
            new=collect(paths,Path(self.temp.name))
            existing=set(map(str,self.paths))
            for p in new:
                if str(p) not in existing:
                    self.paths.append(p); self.items.addItem(p.name); existing.add(str(p))
            self.status.setText(f'{len(self.paths)} valid photographs imported')
            if self.items.currentRow()<0 and self.paths: self.items.setCurrentRow(0)
        except Exception as exc: QMessageBox.warning(self,'Import error',str(exc))
    def preview_current(self): self.preview(self.items.currentRow())
    def preview(self, idx):
        if idx<0 or idx>=len(self.paths): return
        try:
            from PIL import ImageOps
            with Image.open(self.paths[idx]) as source:
                original=ImageOps.exif_transpose(source).convert('RGB'); original.thumbnail((720,720))
            corrected=enhance(original,self.strength.value()/100)
            for im,widget in [(original,self.original),(corrected,self.edited)]:
                data=im.tobytes('raw','RGB'); q=QImage(data,im.width,im.height,im.width*3,QImage.Format_RGB888)
                widget.setPixmap(QPixmap.fromImage(q.copy()).scaled(widget.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
        except Exception as exc: self.status.setText(f'Preview error: {exc}')
    def resizeEvent(self,event):
        super().resizeEvent(event)
        if self.paths: self.preview_current()
    def export(self):
        if not self.paths: QMessageBox.information(self,'No photographs','Import photographs first.'); return
        choice=QMessageBox.question(self,'Export format','Export all enhanced images into a ZIP archive?\nChoose No to export to a folder.',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        if choice==QMessageBox.Cancel: return
        as_zip=choice==QMessageBox.Yes
        if as_zip: dest,_=QFileDialog.getSaveFileName(self,'Save ZIP','enhanced_photos.zip','ZIP archive (*.zip)')
        else: dest=QFileDialog.getExistingDirectory(self,'Choose export folder')
        if not dest: return
        self.worker=BatchWorker(self.paths,dest,self.strength.value()/100,as_zip)
        self.worker.progress.connect(lambda n,name:(self.progress.setValue(n),self.status.setText(f'Processing {name}')))
        self.worker.completed.connect(lambda output:(self.status.setText(f'Export complete: {output}'),QMessageBox.information(self,'Complete',f'Enhanced photographs saved to:\n{output}')))
        self.worker.failed.connect(lambda err:QMessageBox.critical(self,'Export failed',err))
        self.worker.start()
    def closeEvent(self,event):
        if hasattr(self,'worker') and self.worker.isRunning():
            QMessageBox.information(self,'Processing','Please wait for batch processing to finish.'); event.ignore(); return
        self.temp.cleanup(); super().closeEvent(event)

if __name__=='__main__':
    app=QApplication(sys.argv); window=Window(); window.show(); sys.exit(app.exec())
