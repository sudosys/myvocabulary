from PySide6 import QtWidgets
from googletrans import Translator

class Vocabulary:

    def __init__(self, window):
        self.window = window
        self.number_of_words = 0
        self.words = []
        self.pull_vocab()
        self.fill_word_table()
        self.window.word_count.setText(str(self.number_of_words) + " words in total")

    def pull_vocab(self):

        try:
            file_content = open("../../vocabulary.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            file_content = open("../../vocabulary.txt", "w", encoding="utf-8")

        for word in file_content:
            word_pair = word.split(" > ")
            word_pair[1] = word_pair[1].strip("\n")

            self.words.append(word_pair)
            self.number_of_words += 1

    def fill_word_table(self):

        self.window.word_table.setRowCount(len(self.words))

        for row in range(len(self.words)):

            self.window.word_table.setItem(row, 0, QtWidgets.QTableWidgetItem(self.words[row][0]))
            self.window.word_table.setItem(row, 1, QtWidgets.QTableWidgetItem(self.words[row][1]))

            row += 1

        self.window.word_table.resizeRowsToContents()

    def search_word(self, word):

        translator = Translator()

        translated = translator.translate(word, src="en", dest="tr")

        print(translated.text)
