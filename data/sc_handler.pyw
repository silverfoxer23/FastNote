# shortcut handler module

#imports
import sys
import os
import keyboard
import ctypes
import subprocess

# variables
appdata = os.environ['LOCALAPPDATA']+"\\HHAppdata\\Fastnote"
notes_path = os.environ['USERPROFILE']+"\\Documents\\Fastnote"
config_file = appdata+"\\config.txt"

with open(config_file, 'r') as config_file_reader:
    lines = config_file_reader.readlines()
    language = lines[4].strip().split(": ")[1]
    langfile = open("data\\lang\\"+language+".txt").readlines()
    notes_path = lines[5].strip().split(": ")[1]

sc_arg = sys.argv[1]
file_arg = sys.argv[2]

while True:
    keyboard.wait(sc_arg)
    print(sc_arg + langfile[2])
    subprocess.Popen(["pythonw", "winfolder\\"+file_arg])
