import tkinter as tk
import tkinter.ttk as ttk
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
        try: self.open_vocab("r")
        except: self.welcome_popup()
        self.parent.title("MyVocabulary")
        self.word_listbox = tk.Listbox(self.parent, selectmode = "multiple")
        self.word_listbox_scrollbar = ttk.Scrollbar(self.parent)
        self.word_listbox.bind("<Double-Button>", self.listbox_dbclick)
        self.word_fill()
        self.search_word = tk.StringVar()
        self.search_box = ttk.Entry(self.lower_frame, textvariable = self.search_word)
        self.search_button = ttk.Button(self.lower_frame, text = "Search", command = self.search)
        self.remove_button = ttk.Button(self.lower_frame, text = "Remove Selected Word(s)", command = self.remove)
        self.bottom_label = ttk.Label(self.lower_frame, text = "Powered by Google Translate")
        self.gt_icon = ImageTk.PhotoImage(Image.open("icons\\google_translate_icon.ico"))
        self.icon_label = ttk.Label(self.lower_frame, image = self.gt_icon)
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

    def open_vocab(self, mode, return_what = None):

        vocabulary = open("vocabulary.txt", mode, encoding = "utf-8")

        if mode == "r":
        
            file_content = vocabulary.readlines()
            vocabulary.close()

        if return_what == "file_content":
            return file_content
        elif return_what == "vocabulary":
            return vocabulary
    
    def word_fill(self):

        self.word_listbox.delete(0, tk.END)

        file_content = self.open_vocab("r", "file_content")

        for line in file_content:
            self.word_listbox.insert(0, line)
    
    def edit_window(self):

        self.window = tk.Toplevel()

        self.window.geometry("250x110+820+400")

        self.window.title("Editing")

        self.window.iconbitmap("icons\\myvocabulary_icon.ico")

        edited_meaning = tk.StringVar()

        edited_meaning.set(self.translation)

        edit_label = tk.Label(self.window, text = "Type the meaning below")

        edit_entry = tk.Entry(self.window, textvariable = edited_meaning)

        add_button = tk.Button(self.window, text = "Add to Vocabulary", command = lambda: self.add_to_vocab(edited_meaning.get(), editing = True))

        edit_label.pack(pady = 5)

        edit_entry.pack(pady = 5)

        add_button.pack(pady = 5)

        self.window.mainloop()
    
    def duplicate_checker(self):
        
        file_content = self.open_vocab("r", "file_content")

        for line in file_content:

            word = line.split(">")[0].strip()

            if self.search_word.get() == word:
                warning_msg = "This word already exists!\n\n{}".format(line)
                messagebox.showwarning(title = "Warning", message = warning_msg)
                return True
            
        return False
        
    def add_to_vocab(self, word, editing = False):

        if editing: 
            if self.duplicate_checker(): return
        
        vocabulary = self.open_vocab("a", "vocabulary")

        line = "{} > {}\n".format(self.search_word.get(), word)

        vocabulary.write(line)

        vocabulary.close()

        self.word_fill()

        if editing: self.window.destroy()

    def search(self):

        if self.search_word.get() == "":
            messagebox.showerror(title = "Error", message = "You didn't enter any words!")
            return
        
        translator = googletrans.Translator()

        self.translation = (translator.translate(self.search_word.get(), src = "en", dest = "tr").text).lower()

        if self.duplicate_checker(): return

        dialog_msg = "{} > {}\n\nWould you like to add this word to your vocabulary?".format(self.search_word.get(), self.translation)

        dialog_win = messagebox.askyesno(title = "Meaning Found!", message = dialog_msg)

        if dialog_win == True:

            edit_dialog = messagebox.askyesno(title = "Any Edits?", message = "Would you like to edit the meaning of the word?")

            if edit_dialog == True: self.edit_window()

            else: self.add_to_vocab(self.translation)

    def remove(self):

        if len(self.word_listbox.curselection()) == 0:
            messagebox.showerror(title = "Error", message = "You didn't select any words!")
            return
        
        lines_to_delete = [self.word_listbox.get(index) for index in self.word_listbox.curselection()]

        file_content = self.open_vocab("r", "file_content")

        for line_to_delete in lines_to_delete: del file_content[file_content.index(line_to_delete)]

        vocabulary = self.open_vocab("w", "vocabulary")

        for line in file_content: vocabulary.write(line)

        vocabulary.close()

        self.word_fill()

    def listbox_dbclick(self, event):

        if len(self.word_listbox.curselection()) > 1:

            messagebox.showerror(title = "Error", message = "You must select only one word!")
            return

        info_msg = self.word_listbox.get(self.word_listbox.curselection())

        word_meaning = messagebox.showinfo(title = "Word and Its Meaning", message = info_msg)

        if word_meaning == "ok": self.word_listbox.select_clear(0, "end")
        
    def welcome_popup(self):

        self.open_vocab("w")

        messagebox.showinfo(title = "Welcome!",
        message = "Looks like this is the first time you're using MyVocabulary.\nWe've created a \"vocabulary.txt\" file for you, which is where you will be storing your words.")
