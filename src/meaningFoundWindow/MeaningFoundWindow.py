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
        self.loadUi()

    def loadUi(self):
        
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "meaningFoundWindow.ui")

        uiFile = QFile(path)
        uiFile.open(QFile.ReadOnly)
        self.window = loader.load(uiFile, self)

        appIcon = QIcon(QPixmap("../../icons/myvocabulary_icon.png"))
        self.window.setWindowIcon(appIcon)

        uiFile.close()
