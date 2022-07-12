import os
from pathlib import Path

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap


class MeaningFoundWindow(QDialog):

    def __init__(self):
        super(MeaningFoundWindow, self).__init__()
        self.window = None
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "meaning_found_window.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        app_icon = QIcon(QPixmap("../../icons/myvocabulary_icon.png"))
        self.window.setWindowIcon(app_icon)
        ui_file.close()
