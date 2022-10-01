# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meaningFoundWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 190)
        self.yes_button = QPushButton(Dialog)
        self.yes_button.setObjectName(u"yes_button")
        self.yes_button.setGeometry(QRect(320, 160, 80, 24))
        self.no_button = QPushButton(Dialog)
        self.no_button.setObjectName(u"no_button")
        self.no_button.setGeometry(QRect(410, 160, 80, 24))
        self.meaning_found = QLabel(Dialog)
        self.meaning_found.setObjectName(u"meaning_found")
        self.meaning_found.setGeometry(QRect(70, 30, 371, 61))
        self.meaning_found.setAlignment(Qt.AlignCenter)
        self.meaning_found.setWordWrap(True)
        self.word_and_meaning = QLabel(Dialog)
        self.word_and_meaning.setObjectName(u"word_and_meaning")
        self.word_and_meaning.setGeometry(QRect(0, 80, 501, 71))
        self.word_and_meaning.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Meaning Found!", None))
        self.yes_button.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.no_button.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.meaning_found.setText(QCoreApplication.translate("Dialog", u"Meaning found! Would you like to add this word to your vocabulary?Meaning can be edited later in the table", None))
        self.word_and_meaning.setText("")
    # retranslateUi

