# kill handler module

# imports
import os
import sys
import time
import signal
import psutil

# variables
mainpid = int(sys.argv[1])
appdata = os.environ['LOCALAPPDATA'] + "\\HHAppdata\\Fastnote"

while True:
    time.sleep(5)
    if not psutil.pid_exists(mainpid):
        with open(appdata + "\\tempid.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            pid = int(line.strip())
            try:
                os.kill(pid, signal.SIGTERM)
            except OSError as e:
                pass
        os.remove(appdata + "\\tempid.txt")
        sys.exit()
