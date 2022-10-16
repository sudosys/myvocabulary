import os
import sys
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap

sys.path.append("../")

from vocabulary import Vocabulary

class MainWindow(QMainWindow, QTableWidget):

    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.window = None
        self.loadUi()
        self.window.word_count.setAlignment(Qt.AlignCenter)
        self.vocab = Vocabulary(self.window)

        self.window.source_lang.addItems(list(self.vocab.languageOptions.keys()))
        self.window.dest_lang.addItems(list(self.vocab.languageOptions.keys())[1:])

        self.window.source_lang.setCurrentIndex(1)
        self.window.dest_lang.setCurrentIndex(3)

        # GUI element bindings
        self.window.search_box.returnPressed.connect(self.window.search_button.click)
        self.window.search_button.clicked.connect(lambda: self.initSearchWord
        (self.window.search_box.text(), self.window.source_lang.currentIndex(), self.window.dest_lang.currentIndex()+1))
        self.window.delete_button.clicked.connect(self.initDeleteSelectedWords)
        self.window.swap_button.clicked.connect(self.swapSourceAndTarget)
        self.window.source_lang.currentIndexChanged.connect(self.enableDisableSwapButton)
        self.window.dest_lang.currentIndexChanged.connect(self.enableDisableSwapButton)

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
            or (self.window.source_lang.currentIndex()-1 == self.window.dest_lang.currentIndex())):
            self.window.swap_button.setEnabled(False)

    def swapSourceAndTarget(self):

        sourceLangIndex = self.window.source_lang.currentIndex()
        self.window.source_lang.setCurrentIndex(self.window.dest_lang.currentIndex()+1)
        self.window.dest_lang.setCurrentIndex(sourceLangIndex-1)

    def displayDialogMessage(self, title, text, buttons, icon):
        dialog = QtWidgets.QMessageBox(self)
        dialog.setWindowIcon(QIcon(QPixmap("../../icons/myvocabulary_icon.png")))
        dialog.setWindowTitle(title)
        dialog.setText(text)
        dialog.setStandardButtons(buttons)
        dialog.setIcon(icon)
        dialog.exec()

    def initSearchWord(self, word, srcLangIndex, destLangIndex):

        if(not self.window.search_box.text()):
            self.displayDialogMessage("Error", "Search box is empty!", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Critical)
            return

        self.vocab.searchWord(word, srcLangIndex, destLangIndex)

    def initDeleteSelectedWords(self):

        if (not self.window.word_table.selectedIndexes()):
            self.displayDialogMessage("Error", "No words are selected!", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Critical)
            return

        self.vocab.deleteSelectedWords()


if __name__ == "__main__":

    app = QApplication([])
    mainwindow = MainWindow()
    sys.exit(app.exec())
