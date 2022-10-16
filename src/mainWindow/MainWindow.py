import os
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap

import googletrans

sys.path.append("../")

from vocabulary import Vocabulary

class MainWindow(QMainWindow, QTableWidget):

    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.window = None
        self.loadUi()
        
        self.vocab = Vocabulary(self.window)

        self.languageOptions = {"Auto": "auto", "English": "en","Français": "fr","Deutsch": "de","Türkçe": "tr"}

        self.window.source_lang.addItems(list(self.languageOptions.keys()))
        self.window.target_lang.addItems(list(self.languageOptions.keys())[1:])
        self.window.source_lang.setCurrentIndex(1)
        self.window.target_lang.setCurrentIndex(1)

        # GUI element bindings
        self.window.search_box.returnPressed.connect(self.window.search_button.click)
        self.window.search_button.clicked.connect(lambda: self.vocab.searchWord(self.window.search_box.text()))
        self.window.delete_button.clicked.connect(self.vocab.deleteSelectedRows)
        self.window.swap_button.clicked.connect(self.swapSourceAndTarget)
        self.window.source_lang.currentIndexChanged.connect(self.enableDisableSwapButton)
        self.window.target_lang.currentIndexChanged.connect(self.enableDisableSwapButton)

    def loadUi(self):
        
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "mainWindow.ui")
        
        uiFile = QFile(path)
        uiFile.open(QFile.ReadOnly)
        self.window = loader.load(uiFile, self)
        
        appIcon = QIcon(QPixmap("../../icons/myvocabulary_icon.png"))
        self.window.setWindowIcon(appIcon)
        self.window.show()
        uiFile.close()

    def enableDisableSwapButton(self):

        self.window.swap_button.setEnabled(True)

        if (self.window.source_lang.currentIndex() == 0
            or (self.window.source_lang.currentIndex()-1 == self.window.target_lang.currentIndex())):
            self.window.swap_button.setEnabled(False)


    def swapSourceAndTarget(self):

        sourceLangIndex = self.window.source_lang.currentIndex()
        self.window.source_lang.setCurrentIndex(self.window.target_lang.currentIndex()+1)
        self.window.target_lang.setCurrentIndex(sourceLangIndex-1)


if __name__ == "__main__":

    app = QApplication([])
    mainwindow = MainWindow()
    sys.exit(app.exec())
