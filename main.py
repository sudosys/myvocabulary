import tkinter as tk

class MyVocabulary(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()
    
    def initGUI(self):
        self.parent.title("MyVocabulary")
        self.word_listbox = tk.Listbox(self.parent, selectmode = "multiple")
        self.search_box = tk.Entry(self.parent)
        self.search_button = tk.Button(self.parent, text = "Search", command = self.search)
        self.remove_button = tk.Button(self.parent, text = "Remove Selected Word(s)", command = self.remove)
        # Packing #
        self.word_listbox.pack(fill = tk.BOTH, expand = True)
        self.search_box.insert(0, "Search for a word...")
        self.search_box.pack()
        self.search_box.bind("<FocusIn>", lambda x: self.search_box.delete(0, tk.END))
        self.search_button.pack()
    
    def search(self):
        pass
    
    def remove(self):
        pass