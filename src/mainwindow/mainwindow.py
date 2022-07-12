import os
import sys
from pathlib import Path


from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget
from PySide6 import QtCore
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap

sys.path.append("../")

from vocabulary import Vocabulary


class MainWindow(QMainWindow, QTableWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.window = None
        self.load_ui()
        self.vocab = Vocabulary(self.window)
        # GUI element bindings
        self.window.search_box.returnPressed.connect(self.window.search_button.click)
        self.window.search_button.clicked.connect(lambda: self.vocab.search_word(self.window.search_box.text()))
        self.window.delete_button.clicked.connect(self.vocab.delete_selected_rows)

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "mainwindow.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        app_icon = QIcon(QPixmap("../../icons/myvocabulary_icon.png"))
        self.window.setWindowIcon(app_icon)
        self.window.show()
        ui_file.close()


if __name__ == "__main__":

    app = QApplication([])
    mainwindow = MainWindow()
    sys.exit(app.exec())
