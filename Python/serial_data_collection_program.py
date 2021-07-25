'''
Gathers serial data and stores to csv
renamed from toiletagain.py
'''

import serial
import time
import os

project_dir1 = "/Users/Leon/Documents/ToiletProjectUni2021/Python" # Put in the directory of where this program is in
project_dir2 = "/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/papi(hunched)" #Put the directory here of where you want to send it
filename = "papi(hunched)T-9.csv"
h = os.path.join(project_dir1, filename)
ser = serial.Serial('/dev/tty.usbmodem14201', baudrate=9600, timeout=.1) #Put the serial port here.

counter = 0
f = open(filename, "w")

time.sleep(4)
while counter < 156:
    if counter == 0:
        f.write(",".join(['time', 'floor_scale', 'toilet_scale']))
    arduinoData = ser.readline()
    string = arduinoData.decode()
    num = str(string)
    print(num)
    f.write(str(num))
    counter += 1


From1 = (os.path.join(project_dir1, filename))
To1 = (os.path.join(project_dir2, filename))
os.rename(From1,To1)