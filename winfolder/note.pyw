# note module

# imports
import os
import hashlib
import tkinter as tk
from datetime import datetime

# variables
appdata = os.environ['LOCALAPPDATA']+"\\HHAppdata\\Fastnote"
notes_path = os.environ['USERPROFILE']+"\\Documents\\Fastnote"
config_file = appdata+"\\config.txt"

# functions
def on_text_change(event):
    global out
    out = input.get("1.0", "end-1c")

with open(config_file, 'r') as config_file_reader:
    lines = config_file_reader.readlines()
    language = lines[4].strip().split(": ")[1]
    langfile = open("data\\lang\\"+language+".txt").readlines()
    notes_path = lines[5].strip().split(": ")[1]

root = tk.Tk()
root.wm_title(langfile[11])
root.geometry("200x225")
root.wm_resizable(False, False)
root.wm_focusmodel(model="active")
root.configure(
    bg="#ffd646"
)

window = tk.Frame(root)
input = tk.Text(
    root, 
    height = 11, 
    width = 25,
    bg="#ffd646",
    wrap="word",
    font="Arial", 
    bd=0
)
input.pack()
window.pack()

input.bind("<KeyRelease>", on_text_change)

input.focus_set()

root.iconbitmap("data\\src\\icon.ico")
root.mainloop()

file_name = datetime.now().strftime("%d_%m_%H_%M_%S") + out[:10]

if out != "":
    f = open(notes_path+"\\"+file_name+".txt", 'w')
    f.write(out)
    f.close()

    f = open(appdata+"\\backups\\"+file_name+".txt", 'w')
    f.write(out)
    f.write("\nHASHDATA: " + hashlib.sha256(out.encode('utf-8')).hexdigest())
    f.close()
    
    f = open(notes_path+"\\db.txt", '+a')
    f.write("\n" + notes_path+"\\"+file_name+".txt | " + hashlib.sha256(out.encode('utf-8')).hexdigest())
    f.close()
