# first run module

# imports
import os
import tkinter as tk
from tkinter import ttk

# variables
appdata = os.environ['LOCALAPPDATA']+"\\HHAppdata\\Fastnote"
config_file = appdata+"\\config.txt"

with open(config_file, 'r') as config_file_reader:
    lines = config_file_reader.readlines()
    shortcut = lines[1].strip().split(": ")[1]
    sc_open = lines[2].strip().split(": ")[1]
    sc_settings = lines[3].strip().split(": ")[1]
    language = lines[4].strip().split(": ")[1]
    langfile = open("data\\lang\\"+language+".txt").readlines()

# main
root = tk.Tk()
root.wm_title(langfile[3])
root.geometry("700x350")
root.wm_resizable(False, False)
root.wm_focusmodel(model="active")
root.wm_attributes( '-toolwindow', True)

fr0img = tk.PhotoImage(file="data\\src\\fr0.png").subsample(7, 7)
fr0lbl = ttk.Label(image=fr0img).pack()

frame = tk.Frame(root)
frame.pack(side=tk.TOP)

text = tk.Label(root, text="Fastnotes", font="Arial, 30").pack()
text = tk.Label(root, text=langfile[4]).pack()

frame = tk.Frame(root)
frame.pack(side=tk.TOP)

text = tk.Label(frame, text=langfile[5]).pack(side=tk.LEFT)
text = tk.Label(frame, text=shortcut, font='TkFixedFont', background="lightgray").pack(side=tk.LEFT)
text = tk.Label(frame, text=langfile[6]).pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack(side=tk.TOP)

# text = tk.Label(frame, text=langfile[7]).pack(side=tk.LEFT)
# text = tk.Label(frame, text=sc_open, font='TkFixedFont', background="lightgray").pack(side=tk.LEFT)
# text = tk.Label(frame, text=langfile[8]).pack(side=tk.LEFT)
# text = tk.Label(frame, text=sc_settings, font='TkFixedFont', background="lightgray").pack(side=tk.LEFT)
# text = tk.Label(frame, text=langfile[9]).pack(side=tk.LEFT)

tk.Button(
    root, 
    text=langfile[10], 
    command=lambda: root.quit(),
).pack()

root.iconbitmap("data\\src\\icon.ico")
root.mainloop()