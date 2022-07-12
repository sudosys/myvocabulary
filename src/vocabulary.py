from PySide6 import QtWidgets
from googletrans import Translator

from meaning_found_window.meaning_found_window import MeaningFoundWindow

class Vocabulary:

    def __init__(self, window):
        self.window = window
        self.number_of_words = 0
        self.words = []
        self.pull_vocab()
        self.fill_word_table()
        self.window.word_count.setText(str(self.number_of_words) + " words in total")
        self.dialog_window = MeaningFoundWindow()

    def pull_vocab(self):

        try:
            file = open("../../vocabulary.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            file = open("../../vocabulary.txt", "w", encoding="utf-8")

        for word in file:
            word_pair = word.split(" > ")
            word_pair[1] = word_pair[1].strip("\n")

            self.words.append(word_pair)
            self.number_of_words += 1

        file.close()

    def fill_word_table(self):

        self.window.word_table.setRowCount(len(self.words))

        for row in range(len(self.words)):

            self.window.word_table.setItem(row, 0, QtWidgets.QTableWidgetItem(self.words[row][0]))
            self.window.word_table.setItem(row, 1, QtWidgets.QTableWidgetItem(self.words[row][1]))

            row += 1

        self.window.word_table.resizeRowsToContents()
        self.window.word_table.scrollToBottom()

    def search_word(self, word):

        translator = Translator()

        translated = translator.translate(word, src="en", dest="tr").text.lower()

        self.dialog_window.window.word_and_meaning.setText(word + " > " + translated)

        self.dialog_window.window.yes_button.clicked.connect(lambda: self.add_to_vocab(word, translated))
        self.dialog_window.window.no_button.clicked.connect(self.dialog_window.window.close)

        self.dialog_window.window.show()
        self.dialog_window.window.exec()

    def add_to_vocab(self, word_src, word_dest):

        print()
