# first run module

# imports
import os
import tkinter as tk
from tkinter import ttk

# variables
appdata = os.environ['LOCALAPPDATA']+"\\HHAppdata\\Fastnote"
config_file = appdata+"\\config.txt"

# main
root = tk.Tk()
root.wm_title("Welcome")
root.geometry("500x300")
root.wm_resizable(False, False)
# root.wm_attributes( '-toolwindow', True)
root.wm_focusmodel(model="active")


fr0img = tk.PhotoImage(file="data\\src\\fr0.png").subsample(7, 7)
fr0lbl = ttk.Label(image=fr0img).pack()
text = tk.Label(root, text="Info").pack()
# message.grid(row=1, column=0)

root.iconbitmap("data\src\icon.ico")
root.mainloop()