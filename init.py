from main import *

root = tk.Tk()

root.geometry("300x500")

root.iconbitmap("myvocabulary_icon.ico")

app = MyVocabulary(root)

app.mainloop()