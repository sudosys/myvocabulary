import tkinter as tk
from tkinter import messagebox
import googletrans
from PIL import ImageTk, Image

class MyVocabulary(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.lower_frame = tk.Frame(self.parent)
        self.lower_frame.pack(side = tk.BOTTOM)
        self.initGUI()
    
    def initGUI(self):
        self.parent.title("MyVocabulary")
        self.word_listbox = tk.Listbox(self.parent, selectmode = "multiple")
        self.word_listbox_scrollbar = tk.Scrollbar(self.parent)
        self.word_fill()
        self.search_word = tk.StringVar()
        self.search_box = tk.Entry(self.lower_frame, textvariable = self.search_word)
        self.search_button = tk.Button(self.lower_frame, text = "Search", command = self.search)
        self.remove_button = tk.Button(self.lower_frame, text = "Remove Selected Word(s)", command = self.remove)
        self.bottom_label = tk.Label(self.lower_frame, text = "Powered by Google Translate")
        self.gt_icon = ImageTk.PhotoImage(Image.open("icons\\google_translate_icon.ico"))
        self.icon_label = tk.Label(self.lower_frame, image = self.gt_icon)
        # Packings and configurations #
        self.word_listbox.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.word_listbox_scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.word_listbox.config(yscrollcommand = self.word_listbox_scrollbar.set)
        self.word_listbox_scrollbar.config(command = self.word_listbox.yview)
        self.search_box.pack(pady = 10)
        self.search_button.pack(pady = 10)
        self.remove_button.pack(pady = 10)
        self.bottom_label.pack(side = tk.LEFT, pady = 10)
        self.icon_label.pack(side = tk.RIGHT, pady = 10)
    
    def word_fill(self):

        self.word_listbox.delete(0, tk.END)

        vocabulary = open("vocabulary.txt", "r", encoding = "utf-8")

        file_content = vocabulary.readlines()

        for line in file_content:
            self.word_listbox.insert(0, line)
        
        vocabulary.close()

    def search(self):

        if self.search_word.get() == "":
            messagebox.showerror(title = "Error", message = "You didn't enter any words!")
            return
        
        translator = googletrans.Translator()

        self.translation = (translator.translate(self.search_word.get(), src = "en", dest = "tr").text).lower()

        vocabulary = open("vocabulary.txt", "r", encoding = "utf-8")

        file_content = vocabulary.readlines()

        for line in file_content:

            word = line.split(">")[0].strip()

            if self.search_word.get() == word:
                warning_msg = "This word already exists!\n\n{}".format(line)
                messagebox.showwarning(title = "Warning", message = warning_msg)
                vocabulary.close()
                return

        vocabulary.close()

        dialog_msg = "{} > {}\n\nWould you like to add this word to your vocabulary?".format(self.search_word.get(), self.translation)

        dialog_win = messagebox.askyesno(title = "Meaning Found!", message = dialog_msg)

        if dialog_win == True:
    
            vocabulary = open("vocabulary.txt", "a", encoding = "utf-8")

            line = "{} > {}\n".format(self.search_word.get(), self.translation)

            vocabulary.write(line)

            vocabulary.close()

            self.word_fill()

    def remove(self):

        if len(self.word_listbox.curselection()) == 0:
            messagebox.showerror(title = "Error", message = "You didn't select any words!")
            return
        
        for index in self.word_listbox.curselection():

            line_to_delete = self.word_listbox.get(index)

            vocabulary = open("vocabulary.txt", "r", encoding = "utf-8")

            file_content = vocabulary.readlines()

            ctrl = 0

            for line in file_content:

                if line_to_delete == line: del file_content[ctrl]
                
                ctrl += 1

            vocabulary = open("vocabulary.txt", "w", encoding = "utf-8")

            for line in file_content: vocabulary.write(line)

        vocabulary.close()

        self.word_fill()