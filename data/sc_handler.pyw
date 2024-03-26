# shortcut handler module

# imports
import os
import sys
import keyboard
import subprocess

# variables
appdata = os.environ['LOCALAPPDATA'] + "\\HHAppdata\\Fastnote"
notes_path = os.environ['USERPROFILE'] + "\\Documents\\Fastnote"
config_file = appdata + "\\config.txt"
sc_arg = sys.argv[1]
file_arg = sys.argv[2]

with open(config_file, 'r') as config_file_reader:
    lines = config_file_reader.readlines()
    language = lines[4].strip().split(": ")[1]
    langfile = open("data\\lang\\"+language+".txt").readlines()
    notes_path = lines[5].strip().split(": ")[1]

f = open(appdata+"\\tempid.txt", '+a')
f.write(str(os.getpid()) + "\n")
f.close()

# main
while True:
    keyboard.wait(sc_arg)
    print(sc_arg + langfile[2])
    subprocess.Popen(["pythonw", "winfolder\\"+file_arg])
