from PySide6 import QtWidgets
from googletrans import Translator

from meaningFoundWindow.MeaningFoundWindow import MeaningFoundWindow

class Vocabulary:

    def __init__(self, window):
        
        self.window = window
        self.numberOfWords = 0
        self.words = []
        self.translator = Translator()
        
        self.fillWordTable()
        
        self.dialogWindow = MeaningFoundWindow()
        self.dialogWindow.window.yes_button.clicked.connect(lambda: self.addToVocab(self.window.search_box.text(), self.translated))
        self.dialogWindow.window.no_button.clicked.connect(self.dialogWindow.window.close)
        self.window.word_table.itemChanged.connect(self.updateMeaning)

    def fetchVocab(self):

        self.words = []
        self.numberOfWords = 0
        self.window.word_table.setRowCount(self.numberOfWords)

        try:
            file = open("../../vocabulary.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            file = open("../../vocabulary.txt", "w", encoding="utf-8")

        for word in file:
            word_pair = word.split(" > ")
            word_pair[1] = word_pair[1].strip("\n")

            self.words.append(word_pair)
            self.numberOfWords += 1

        file.close()

    def deleteSelectedRows(self):

        rowsToDelete = list(set([index.row() for index in self.window.word_table.selectedIndexes()]))
        rowsToDelete.sort(reverse=True)
        
        print(self.window.word_table.item(1609,0).text())

        for row in rowsToDelete:
            self.window.word_table.removeRow(row)
            del self.words[row]
            self.numberOfWords -= 1

        self.updateVocab()

    def updateWordCountLabel(self):
        self.window.word_count.setText(str(self.numberOfWords) + " words in total")

    def fillWordTable(self):

        self.fetchVocab()

        self.window.word_table.setRowCount(self.numberOfWords)

        for row in range(self.numberOfWords):

            self.window.word_table.setItem(row, 0, QtWidgets.QTableWidgetItem(self.words[row][0]))
            self.window.word_table.setItem(row, 1, QtWidgets.QTableWidgetItem(self.words[row][1]))

        self.window.word_table.resizeRowsToContents()
        self.window.word_table.scrollToBottom()

        self.updateWordCountLabel()

    def updateVocab(self):
        
        file = open("../../vocabulary.txt", "w", encoding="utf-8")

        for word in self.words:
            file.write(word[0] + " > " + word[1] + "\n")

        file.close()

        self.updateWordCountLabel()

    def searchWord(self, word):

        translated = self.translator.translate(word, src="en", dest="tr").text.lower()

        self.dialogWindow.window.word_and_meaning.setText(word + " > " + translated)

        self.dialogWindow.window.exec()

    def addToWordTable(self, word, meaning):

        self.words.append([word, meaning])
        self.numberOfWords += 1

        self.window.word_table.setRowCount(self.numberOfWords)

        self.window.word_table.setItem(self.numberOfWords-1, 0, QtWidgets.QTableWidgetItem(self.words[self.numberOfWords-1][0]))
        self.window.word_table.setItem(self.numberOfWords-1, 1, QtWidgets.QTableWidgetItem(self.words[self.numberOfWords-1][1]))
    
    def addToVocab(self, word_src, word_dest):

        file = open("../../vocabulary.txt", "a", encoding="utf-8")

        file.write(word_src + " > " + word_dest + "\n")

        file.close()

        self.dialogWindow.window.close()

        self.addToWordTable(word_src, word_dest)

        self.window.word_table.scrollToBottom()

        self.updateWordCountLabel()

    def updateMeaning(self):
        
        currentCell = self.window.word_table.selectedItems()[0]

        updatedMeaning = currentCell.text().encode("utf-8").decode("utf-8")

        self.words[currentCell.row()][1] = updatedMeaning

        self.updateVocab()
        