import tkinter as tk
from gui import create_gui


root = tk.Tk()
root.title("Snake Water Gun")
root.geometry("400x500")
root.resizable(False, False)

create_gui(root)

root.mainloop()