from PySide6 import QtWidgets
from googletrans import Translator

from meaning_found_window.meaning_found_window import MeaningFoundWindow

class Vocabulary:

    def __init__(self, window):
        self.window = window
        self.number_of_words = 0
        self.words = []
        self.translator = Translator()
        
        self.fill_word_table()
        
        self.dialog_window = MeaningFoundWindow()
        self.dialog_window.window.yes_button.clicked.connect(lambda: self.add_to_vocab(self.window.search_box.text(), self.translated))
        self.dialog_window.window.no_button.clicked.connect(self.dialog_window.window.close)

    def fetch_vocab(self):

        self.words = []
        self.number_of_words = 0
        self.window.word_table.setRowCount(self.number_of_words)

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

    def delete_selected_rows(self):

        rows_to_delete = list(set([index.row() for index in self.window.word_table.selectedIndexes()]))
        rows_to_delete.sort(reverse=True)
        
        print(rows_to_delete)
        
        for row in rows_to_delete:
            self.window.word_table.removeRow(row)
            del self.words[row]
            self.number_of_words -= 1

        self.update_vocab()

    def update_word_count_label(self):
        self.window.word_count.setText(str(self.number_of_words) + " words in total")

    def fill_word_table(self):

        self.fetch_vocab()

        self.window.word_table.setRowCount(self.number_of_words)

        for row in range(self.number_of_words):

            self.window.word_table.setItem(row, 0, QtWidgets.QTableWidgetItem(self.words[row][0]))
            self.window.word_table.setItem(row, 1, QtWidgets.QTableWidgetItem(self.words[row][1]))

        self.window.word_table.resizeRowsToContents()
        self.window.word_table.scrollToBottom()

        self.update_word_count_label()

    def update_vocab(self):
        
        file = open("../../vocabulary.txt", "w", encoding="utf-8")

        for word in self.words:
            file.write(word[0] + " > " + word[1] + "\n")

        file.close()

        self.update_word_count_label()

    def search_word(self, word):

        translated = self.translator.translate(word, src="en", dest="tr").text.lower()

        self.dialog_window.window.word_and_meaning.setText(word + " > " + translated)

        self.dialog_window.window.show()
        self.dialog_window.window.exec()

    def add_to_word_table(self, word, meaning):

        self.words.append([word, meaning])
        self.number_of_words += 1

        self.window.word_table.setRowCount(self.number_of_words)

        self.window.word_table.setItem(self.number_of_words-1, 0, QtWidgets.QTableWidgetItem(self.words[self.number_of_words-1][0]))
        self.window.word_table.setItem(self.number_of_words-1, 1, QtWidgets.QTableWidgetItem(self.words[self.number_of_words-1][1]))
    
    def add_to_vocab(self, word_src, word_dest):

        file = open("../../vocabulary.txt", "a", encoding="utf-8")

        file.write(word_src + " > " + word_dest + "\n")

        file.close()

        self.dialog_window.window.close()

        self.add_to_word_table(word_src, word_dest)

        self.window.word_table.scrollToBottom()

        self.update_word_count_label()
