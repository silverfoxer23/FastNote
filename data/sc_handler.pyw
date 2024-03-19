# shortcut handler module

# imports
import os
import sys
import psutil
import keyboard
import threading
import subprocess

# variables
appdata = os.environ['LOCALAPPDATA'] + "\\HHAppdata\\Fastnote"
notes_path = os.environ['USERPROFILE'] + "\\Documents\\Fastnote"
config_file = appdata + "\\config.txt"
sc_arg = sys.argv[1]
file_arg = sys.argv[2]
mainpid = int(sys.argv[3])

def check_mainpid():
    while True:
        if not psutil.pid_exists(mainpid):
            sys.exit()

# start the new thread
threading.Thread(target=check_mainpid).start()

with open(config_file, 'r') as config_file_reader:
    lines = config_file_reader.readlines()
    language = lines[4].strip().split(": ")[1]
    langfile = open("data\\lang\\"+language+".txt").readlines()
    notes_path = lines[5].strip().split(": ")[1]

while True:
    keyboard.wait(sc_arg)
    print(sc_arg + langfile[2])
    subprocess.Popen(["pythonw", "winfolder\\"+file_arg])
