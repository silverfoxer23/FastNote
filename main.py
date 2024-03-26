# @horahenaripo en GitHub

# imports
import os
import sys
import ctypes
import keyboard
import subprocess

# variables
version = "0.6.0 ALPHA"
build = "24032410"
appdata = os.environ['LOCALAPPDATA']+"\\HHAppdata\\Fastnote"
notes_path = os.environ['USERPROFILE']+"\\Documents\\Fastnote"
config_file = appdata+"\\config.txt"
shortcut = 'shift + alt + n'
sc_open = 'shift + alt + o'
sc_settings = 'shift + alt + s'
language = 'eng'
langfile = open("data\\lang\\"+language+".txt").readlines()
pidmain = os.getpid()

# functions
def msgbox(title, text):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def restore_settings():
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
    os.mkdir(appdata)
    os.mkdir(appdata+"\\backups")

# * config data
config = [
    "Version: {0}_{1}".format(version, build),
    "Keyboard: " + shortcut,
    "Open shortcut: " + sc_open,
    "Settings shortcut: " + sc_settings,
    "Language: " + language,
    "NotesPath: " + notes_path
]

# * create config file
if not os.path.exists(config_file):
    restore_settings()
    first_run()
else:
    with open(config_file, 'r') as config_file_reader:
        lines = config_file_reader.readlines()
    if len(lines) == 6:
        shortcut = lines[1].strip().split(": ")[1]
        sc_open = lines[2].strip().split(": ")[1]
        sc_settings = lines[3].strip().split(": ")[1]
        language = lines[4].strip().split(": ")[1]
        langfile = open("data\\lang\\"+language+".txt").readlines()
        notes_path = lines[5].strip().split(": ")[1]
    else:
        msgbox("Error", "The configuration file is incomplete, configuration will be restored to default settings.")
        os.remove(config_file)
        restore_settings()

# TODO RECOVERY SETTINGS

# main
print(langfile[1])

index = 0
y = ["open.py", "settings.py"]
for x in [sc_open, sc_settings]:
    # shortcut, file to open, pid
    subprocess.Popen([ "python", "data\\sc_handler.pyw", x, y[index] ], creationflags=subprocess.BELOW_NORMAL_PRIORITY_CLASS)
    index+=1

subprocess.Popen([ "python", "data\\kill_handler.pyw", str(pidmain) ], creationflags=subprocess.BELOW_NORMAL_PRIORITY_CLASS)

while True:
    keyboard.wait(shortcut)
    print(shortcut + langfile[2])
    subprocess.Popen(["pythonw", "winfolder\\note.pyw"])
