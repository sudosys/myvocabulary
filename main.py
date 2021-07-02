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
        self.word_listbox.bind("<Double-Button>", self.listbox_dbclick_window)
        self.word_listbox.bind("<Delete>", self.remove)
        self.search_box.pack(pady = 10)
        self.placeholder_text = "Type here to search..."
        self.search_word.set(self.placeholder_text)
        self.entry_focus_binding(True)
        self.search_box.bind("<Return>", self.search)
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
    
    def entry_focus_binding(self, binding):

        if binding == True: self.search_box.bind("<FocusIn>", lambda event: self.search_word.set(""))
        
        elif binding == False: self.search_box.unbind("<FocusIn>")

    def add_to_vocab_window(self):

        self.add_window = tk.Toplevel()

        self.add_window.geometry("365x140+760+400")

        self.add_window.title("Meaning Found!")

        self.add_window.iconbitmap("icons\\myvocabulary_icon.ico")

        self.add_window.resizable(False, False)

        question_label = ttk.Label(self.add_window, text = "{} > {}\n\nWould you like to add this word to your vocabulary?".format(self.search_word.get(), self.translation))

        yes_button = ttk.Button(self.add_window, text = "Yes", command = lambda: [self.add_to_vocab(self.translation, external = self.add_window), self.search_box.delete(0, "end"), self.entry_focus_binding(True)])
        edit_button = ttk.Button(self.add_window, text = "Edit", command = self.edit_meaning_window)
        no_button = ttk.Button(self.add_window, text = "No", command = lambda: [self.add_window.destroy(), self.search_box.delete(0, "end"), self.entry_focus_binding(True)])

        question_label.place(relx = 0.5, rely = 0.4, anchor = tk.CENTER)
        no_button.place(relx = 1.0, rely = 1.0, anchor = tk.SE)
        edit_button.place(relx = 0.75, rely = 1.0, anchor = tk.SE)
        yes_button.place(relx = 0.5, rely = 1.0, anchor = tk.SE)

        self.add_window.mainloop()
    
    def edit_meaning_window(self):

        self.add_window.destroy()

        edit_window = tk.Toplevel()

        edit_window.geometry("250x110+820+400")

        edit_window.title("Editing")

        edit_window.iconbitmap("icons\\myvocabulary_icon.ico")

        edit_window.resizable(False, False)

        edited_meaning = tk.StringVar()

        edited_meaning.set(self.translation)

        edit_label = ttk.Label(edit_window, text = "Type the meaning below")

        edit_entry = ttk.Entry(edit_window, textvariable = edited_meaning)

        edit_entry.bind("<Return>", lambda event = None: self.add_to_vocab(edited_meaning.get(), external = edit_window))

        add_button = ttk.Button(edit_window, text = "Add to Vocabulary", command = lambda: self.add_to_vocab(edited_meaning.get(), external = edit_window))

        edit_label.pack(pady = 5)

        edit_entry.pack(pady = 5)

        add_button.pack(pady = 5)

        edit_window.mainloop()
    
    def listbox_dbclick_window(self, event):

        if len(self.word_listbox.curselection()) > 1:
            messagebox.showerror(title = "Error", message = "You must select only one word!")
            return

        dbclick_window = tk.Toplevel()

        dbclick_window.geometry("365x140+760+400")

        dbclick_window.title("Word and Its Meaning")

        dbclick_window.iconbitmap("icons\\myvocabulary_icon.ico")

        dbclick_window.resizable(False, False)

        word_meaning_label = ttk.Label(dbclick_window, text = self.word_listbox.get(self.word_listbox.curselection()), wraplength = 350, justify = tk.CENTER)
        ok_button = ttk.Button(dbclick_window, text = "OK", command = lambda: [dbclick_window.destroy(), self.word_listbox.select_clear(0, "end")])

        word_meaning_label.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        ok_button.place(relx = 1.0, rely = 1.0, anchor = tk.SE)

        dbclick_window.mainloop()

    def duplicate_checker(self):
        
        file_content = self.open_vocab("r", "file_content")

        for line in file_content:

            word = line.split(">")[0].strip()

            if self.search_word.get() == word:
                warning_msg = "This word already exists!\n\n{}".format(line)
                messagebox.showwarning(title = "Warning", message = warning_msg)
                return True
            
        return False
        
    def add_to_vocab(self, word, external = None):

        vocabulary = self.open_vocab("a", "vocabulary")

        line = "{} > {}\n".format(self.search_word.get(), word)

        vocabulary.write(line)

        vocabulary.close()

        self.word_fill()

        if external:
            self.search_box.delete(0, "end")
            external.destroy()

    def search(self, event = None):

        self.entry_focus_binding(False)

        if self.search_word.get() == "" or self.search_word.get() == self.placeholder_text:
            messagebox.showerror(title = "Error", message = "You didn't enter any words!")
            self.entry_focus_binding(True)
            return
        
        translator = googletrans.Translator()

        self.translation = (translator.translate(self.search_word.get(), src = "en", dest = "tr").text).lower()

        if self.duplicate_checker():
            self.search_box.delete(0, "end")
            return

        self.add_to_vocab_window()

    def remove(self, event = None):

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
        
    def welcome_popup(self):

        self.open_vocab("w")

        messagebox.showinfo(title = "Welcome!",
        message = "Looks like this is the first time you're using MyVocabulary.\nWe've created a \"vocabulary.txt\" file for you, which is where you will be storing your words.")