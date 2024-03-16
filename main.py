# @horahenaripo en GitHub

# imports
import os
import sys
import ctypes
import keyboard
import tkinter as tk
import subprocess

# variables
version = "0.2.0 ALPHA"
appdata = os.environ['LOCALAPPDATA']+"\\HHAppdata\\Fastnote"
config_file = appdata+"\\config.txt"
shortcut = 'alt + n'
language = 'esp'

# functions
def msgbox(title, text):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def restore_sett():
    try:
        with open(config_file, 'w') as f:
            f.write('\n'.join(config)) 
    except:
        msgbox("Error", "Unable to create a configuration file")
        sys.exit()

def first_run():
    subprocess.Popen(["pythonw", "winfolder\\first_run.pyw"])


# config
# * create appdata folder
if not os.path.exists(appdata):
    print("Creating folders...")
    os.mkdir(appdata)

# * create config file
if not os.path.exists(config_file):
    print("Creating config files...")
    config = [
        "Version:" + version,
        "Keyboard:" + shortcut,
        "Language:" + language
    ]
    restore_sett()
    first_run()
else:
    with open(config_file, 'r') as f:
        lines = f.readlines()
    if len(lines) >= 2:  
        shortcut = lines[1].strip().split(":")[1]
    else:
        msgbox("Error", "The configuration file is incomplete, configuration will be restored to default settings.")
        os.remove(config_file)
        restore_sett()

# main
print("Running...")
first_run()

while True:
    keyboard.wait(shortcut)
    print(shortcut + ' detected!')

    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')

    message = tk.Label(root, text="Hello, World!")
    message.pack()

    root.iconbitmap("data\\src\\icon.ico")
    root.mainloop()