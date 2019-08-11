import subprocess
import xml.etree.ElementTree as ET
from subprocess import Popen, PIPE

'''
Made by @Scuffedbots on Instagram

To Truly Make This One-Click-Only You Must:
    1. pip install pyinstaller
    2. compile this python file using the command:
        pyinstaller --onefile --debug --clean
    3. now it's an executable that you can click on, when it opens you must type in your device's last part of its local ip (for example 150 or 2 or 3)
        (you can make it more of a oneclick if you set a constant local ip for your phone in which replace the input() line below with a string of that last number of ur local ip)
    4. EXTRA rename this .exe file into something short like a.exe and add it to your environment variables (press windows key and search system env) and this way u can run the program from the run box!
        the program will automatically close when a connection has been established.
'''

DEVICE_NAME = 'FUH0216A14007338' # Can be found using 'adb devices' when phone is plugged
WIFI_LOCAL_IP_SHAPE = '192.168.1.'
WIFI_LOCAL_IP_BUT_ONLY_LAST_PART_OF_THE_LOCAL_IP = input('local ip last number (ex. 2 or 254 or 114) : ')
PORT = '5555'

still = True
while still:
    p = Popen('adb kill-server', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    p = Popen('adb -s ' + DEVICE_NAME + ' connect ' + WIFI_GENERAL_ADDRESS + WIFI_LOCAL_IP_BUT_ONLY_LAST_PART_OF_THE_LOCAL_IP + ':' + PORT, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"no")
    print(err)
    if str(output).find("start") > -1:
        while still:
            p = Popen('adb -s ' + DEVICE_NAME + ' connect ' + WIFI_GENERAL_ADDRESS + WIFI_LOCAL_IP_BUT_ONLY_LAST_PART_OF_THE_LOCAL_IP + ':' + PORT, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"no")
            print(err)
            if str(output).find("connected") > -1:
                print('Connected')
                still = False
