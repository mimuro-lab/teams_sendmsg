from time import sleep
from subprocess import Popen

Popen("chrome.bat")
sleep(1)
Popen(["python", "send_msg.py"])