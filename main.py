# @horahenaripo en GitHub

# imports
import os
import sys
import ctypes
import keyboard
import tkinter as tk

# variables
version = "0.1.0 ALPHA"
appdata = os.environ['LOCALAPPDATA']+"\\HHAppdata"
config_file = appdata+"\\config.txt"
shortcut = 'ctrl + alt + u'

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
        "Keyboard:" + shortcut
    ]
    restore_sett()
else:
    with open(config_file, 'r') as f:
        lines = f.readlines()
    line3_content = None
    if len(lines) >= 1:  
        shortcut = lines[1].strip().split(":")[1]
    else:
        msgbox("Error", "The configuration file is incomplete, configuration will be restored to default settings.")
        os.remove(config_file)
        restore_sett()

# * Main code

print("Running...")

while True:
    keyboard.wait(shortcut)
    print(shortcut + ' detected!')

    root = tk.Tk()

    message = tk.Label(root, text="Hello, World!")
    message.pack()

    root.iconbitmap("data\icon.ico")
    root.mainloop()