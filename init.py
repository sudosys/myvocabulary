from main import *

root = tk.Tk()

root.geometry("300x600")

root.resizable(False, False)

root.iconbitmap("icons\\myvocabulary_icon.ico")

app = MyVocabulary(root)

app.mainloop()