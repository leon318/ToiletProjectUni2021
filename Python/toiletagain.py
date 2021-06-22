

#read the serial data and print it as line
import serial
import time
import os
import shutil
from pathlib import Path

ser = serial.Serial('/dev/tty.usbmodem14201', baudrate=9600, timeout=.1)

weight = [5]
counter = 0
f = open("Experiment1,T10", "w")
time.sleep(3)
while counter < 200:
    arduinoData = ser.readline()
    string = arduinoData.decode()  # convert the byte string to a unicode string
    num = str(string)  # convert the unicode string to an int
    print(num)
    weight.append(num)
    f.write(str(num))
    f.write(str("\n"))
    counter += 1
From1 = "/Users/Leon/Documents/ToiletProjectUni2021/Python/Experiment1,T10"
To1 = "/Users/Leon/Documents/ToiletProjectUni2021/Experiment1(Leon_Standing)/Experiment1,T10"
os.rename(From1,To1)



# 2nd Commit