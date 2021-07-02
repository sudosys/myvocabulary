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
        self.parent.title("MyVocabulary")
        self.word_listbox = tk.Listbox(self.parent, selectmode = "multiple")
        self.word_listbox_scrollbar = ttk.Scrollbar(self.parent)
        self.search_word = tk.StringVar()
        self.search_box = ttk.Entry(self.lower_frame, textvariable = self.search_word, width = 50)
        self.search_button = ttk.Button(self.lower_frame, text = "Search", command = self.search)
        self.remove_button = ttk.Button(self.lower_frame, text = "Remove Selected Word(s)", command = self.remove)
        self.src_lang_label = ttk.Label(self.lower_frame, text = "Source Language")
        self.src_lang, self.src_lang_code = tk.StringVar(), tk.StringVar()
        self.langs = {"Auto": "auto", "English": "en", "Turkish (Türkçe)": "tr", "French (Français)": "fr", "German (Deutsch)": "de"}
        self.src_lang_combobox = ttk.Combobox(self.lower_frame, width = 15, state = "readonly", values = list(self.langs.keys()), textvariable = self.src_lang)
        self.dest_lang_label = ttk.Label(self.lower_frame, text = "Target Language")
        self.dest_lang, self.dest_lang_code = tk.StringVar(), tk.StringVar()
        self.dest_lang_combobox = ttk.Combobox(self.lower_frame, width = 15, state = "readonly", values = list(self.langs.keys())[1:], textvariable = self.dest_lang)
        self.lang_swap_button = ttk.Button(self.lower_frame, text = "<>", width = 3, command = self.lang_swap)
        self.bottom_label = ttk.Label(self.lower_frame, text = "Powered by Google Translate")
        self.gt_icon = ImageTk.PhotoImage(Image.open("icons\\google_translate_icon.ico"))
        self.icon_label = ttk.Label(self.lower_frame, image = self.gt_icon)
        # Widget placements and configurations
        self.word_listbox.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.word_listbox_scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.word_listbox.config(yscrollcommand = self.word_listbox_scrollbar.set)
        self.word_listbox_scrollbar.config(command = self.word_listbox.yview)
        self.word_listbox.bind("<Double-Button>", self.listbox_dbclick_window)
        self.word_listbox.bind("<Delete>", self.remove)
        self.search_box.grid(row = 0, column = 0, columnspan = 3, pady = 10)
        self.placeholder_text = "Type here to search..."
        self.search_word.set(self.placeholder_text)
        self.search_box.bind("<FocusIn>", lambda event: self.search_word.set(""))
        self.search_box.bind("<FocusOut>", self.focusout_behaviour)
        self.search_box.bind("<Return>", self.search)
        self.search_button.grid(row = 1, column = 0, columnspan = 3, pady = 10)
        self.remove_button.grid(row = 2, column = 0, columnspan = 3, pady = 10)
        self.src_lang_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.dest_lang_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.src_lang_combobox.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.src_lang_combobox.current(1)
        self.src_lang_combobox.bind("<<ComboboxSelected>>", lambda event: self.src_lang_code.set(self.langs[self.src_lang.get()]))
        self.lang_swap_button.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.dest_lang_combobox.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.dest_lang_combobox.current(1)
        self.dest_lang_combobox.bind("<<ComboboxSelected>>", lambda event: self.dest_lang_code.set(self.langs[self.dest_lang.get()]))
        self.bottom_label.grid(row = 5, column = 0, columnspan = 3, pady = 10)
        self.icon_label.grid(row = 6, column = 0, columnspan = 3, pady = 10)
        # Checking if "vocabulary.txt" exists, otherwise launch welcome popup
        try: self.open_vocab("r")
        except FileNotFoundError:
            self.open_vocab("w")
            messagebox.showinfo(title = "Welcome!",
            message = "Looks like this is the first time you're using MyVocabulary.\nWe've created a \"vocabulary.txt\" file for you, which is where you will be storing your words.")
        
        self.word_fill()
        # Initially setting default language codes
        self.src_lang_code.set(self.langs[self.src_lang.get()])
        self.dest_lang_code.set(self.langs[self.dest_lang.get()])

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
    
    def focusout_behaviour(self, event):

        if self.search_word.get() != self.placeholder_text and self.search_word.get() != "": return

        elif self.search_word.get() == "": self.search_word.set(self.placeholder_text)
    
    def lang_swap(self):

        if self.src_lang_combobox.current() == 0: self.src_lang_combobox.current(self.src_lang_combobox.current()+1)
        
        temp_index = self.src_lang_combobox.current()
        temp_lang = self.src_lang.get()

        self.src_lang_combobox.current(self.dest_lang_combobox.current()+1)
        self.src_lang_code.set(self.langs[self.dest_lang.get()])

        self.dest_lang_combobox.current(temp_index-1)
        self.dest_lang_code.set(self.langs[temp_lang])

    def add_to_vocab_window(self):

        self.add_window = tk.Toplevel()

        self.add_window.geometry("365x140+780+500")

        self.add_window.title("Meaning Found!")

        self.add_window.iconbitmap("icons\\myvocabulary_icon.ico")

        self.add_window.resizable(False, False)

        if self.src_lang_code.get() == "auto": self.src_lang.set(googletrans.LANGUAGES[self.translation.src].capitalize())

        question_label = ttk.Label(self.add_window, text = "{}: {}\n\n{}: {}\n\nWould you like to add this word to your vocabulary?".format(self.src_lang.get(), self.search_word.get(), self.dest_lang.get(), self.translation.text.lower()), wraplength = 350, justify = tk.CENTER)

        yes_button = ttk.Button(self.add_window, text = "Yes", command = lambda: [self.add_to_vocab(self.translation.text.lower(), external = self.add_window), self.search_box.delete(0, "end")])
        edit_button = ttk.Button(self.add_window, text = "Edit", command = self.edit_meaning_window)
        no_button = ttk.Button(self.add_window, text = "No", command = lambda: [self.add_window.destroy(), self.search_box.delete(0, "end")])

        question_label.place(relx = 0.5, rely = 0.4, anchor = tk.CENTER)
        no_button.place(relx = 1.0, rely = 1.0, anchor = tk.SE)
        edit_button.place(relx = 0.75, rely = 1.0, anchor = tk.SE)
        yes_button.place(relx = 0.5, rely = 1.0, anchor = tk.SE)

        self.add_window.focus_set()
        self.add_window.grab_set()

        self.add_window.mainloop()
    
    def edit_meaning_window(self):

        self.add_window.destroy()

        edit_window = tk.Toplevel()

        edit_window.geometry("250x110+840+500")

        edit_window.title("Editing")

        edit_window.iconbitmap("icons\\myvocabulary_icon.ico")

        edit_window.resizable(False, False)

        edited_meaning = tk.StringVar()

        edited_meaning.set(self.translation.text.lower())

        edit_label = ttk.Label(edit_window, text = "Type the meaning below")

        edit_entry = ttk.Entry(edit_window, textvariable = edited_meaning)

        edit_entry.bind("<Return>", lambda event = None: self.add_to_vocab(edited_meaning.get(), external = edit_window))

        add_button = ttk.Button(edit_window, text = "Add to Vocabulary", command = lambda: self.add_to_vocab(edited_meaning.get(), external = edit_window))

        edit_label.pack(pady = 5)

        edit_entry.pack(pady = 5)

        add_button.pack(pady = 5)

        edit_window.focus_set()
        edit_window.grab_set()

        edit_window.mainloop()
    
    def listbox_dbclick_window(self, event):

        if len(self.word_listbox.curselection()) > 1:
            messagebox.showerror(title = "Error", message = "You must select only one word!")
            return

        dbclick_window = tk.Toplevel()

        dbclick_window.geometry("365x140+780+500")

        dbclick_window.title("Word and Its Meaning")

        dbclick_window.iconbitmap("icons\\myvocabulary_icon.ico")

        dbclick_window.resizable(False, False)

        word_meaning_label = ttk.Label(dbclick_window, text = self.word_listbox.get(self.word_listbox.curselection()), wraplength = 350, justify = tk.CENTER)
        ok_button = ttk.Button(dbclick_window, text = "OK", command = lambda: [dbclick_window.destroy(), self.word_listbox.select_clear(0, "end")])

        word_meaning_label.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        ok_button.place(relx = 1.0, rely = 1.0, anchor = tk.SE)

        dbclick_window.focus_set()
        dbclick_window.grab_set()

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

        if self.search_word.get() == "" or self.search_word.get() == self.placeholder_text:
            messagebox.showerror(title = "Error", message = "You didn't enter any words!")
            return
        
        translator = googletrans.Translator()

        self.translation = (translator.translate(self.search_word.get(), src = self.src_lang_code.get(), dest = self.dest_lang_code.get()))

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