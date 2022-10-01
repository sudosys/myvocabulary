import os
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap

sys.path.append("../")

from Vocabulary import Vocabulary

class MainWindow(QMainWindow, QTableWidget):

    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.window = None
        self.loadUi()
        
        self.vocab = Vocabulary(self.window)
        
        # GUI element bindings
        self.window.search_box.returnPressed.connect(self.window.search_button.click)
        self.window.search_button.clicked.connect(lambda: self.vocab.searchWord(self.window.search_box.text()))
        self.window.delete_button.clicked.connect(self.vocab.deleteSelectedRows)

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

if __name__ == "__main__":

    app = QApplication([])
    mainwindow = MainWindow()
    sys.exit(app.exec())