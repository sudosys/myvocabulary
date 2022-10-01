# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 650)
        MainWindow.setMinimumSize(QSize(450, 650))
        MainWindow.setMaximumSize(QSize(450, 650))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(300, 520, 80, 24))
        self.search_box = QLineEdit(self.centralwidget)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(60, 520, 231, 24))
        self.word_count = QLabel(self.centralwidget)
        self.word_count.setObjectName(u"word_count")
        self.word_count.setGeometry(QRect(180, 630, 171, 20))
        self.word_table = QTableWidget(self.centralwidget)
        if (self.word_table.columnCount() < 2):
            self.word_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.word_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.word_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.word_table.setObjectName(u"word_table")
        self.word_table.setGeometry(QRect(0, 0, 450, 500))
        self.word_table.setMinimumSize(QSize(450, 500))
        self.word_table.setMaximumSize(QSize(450, 500))
        self.word_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.word_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.word_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.word_table.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.word_table.setGridStyle(Qt.DashLine)
        self.word_table.horizontalHeader().setVisible(True)
        self.word_table.horizontalHeader().setCascadingSectionResizes(True)
        self.word_table.horizontalHeader().setDefaultSectionSize(100)
        self.word_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.word_table.horizontalHeader().setStretchLastSection(True)
        self.word_table.verticalHeader().setStretchLastSection(True)
        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(60, 570, 131, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MyVocabulary", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_box.setText("")
        self.search_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here to search online...", None))
        self.word_count.setText("")
        ___qtablewidgetitem = self.word_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        ___qtablewidgetitem1 = self.word_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Turkish", None));
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Words", None))
    # retranslateUi

