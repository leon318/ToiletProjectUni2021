'''
Gathers serial data and stores to csv
'''

import serial
import time
import pandas as pd
from pandas import read_csv
import os
import csv
project_dir1 = "/Users/Leon/Documents/ToiletProjectUni2021/Python" # Put in the directory of where this program is in
project_dir2 = "/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/laura(hunched)" #Put the directory here of where you want to send it
filename = "laura(hunched)T-9.csv"
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

#f.to_csv("Exp5,T-11.csv", header=['Time', 'Floorscale', 'Toilet Scale'], index=False)

# with open(h, 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(["Time", "Toiletscale"])
#     with open(h, 'r') as f:
#             reader = csv.reader(f)
#             writer.writerows(row for row in reader)
    # with open(h, 'r', newline='') as f:
    #         reader = csv.reader(f)
    #         writer.writerows(row[:1] + row[1:] for row in reader)
From1 = (os.path.join(project_dir1, filename))
To1 = (os.path.join(project_dir2, filename))
os.rename(From1,To1)



#with open("/Users/Leon/Documents/ToiletProjectUni2021/Experiment2(Leon_Standing_ADS)/Experiment2,T-1100.csv") as f:
 #   lines = f.readlines()  # read
#lines[0] = ("0.0" + "\n")  # you can replace zero with any line number
#with open("/Users/Leon/Documents/ToiletProjectUni2021/Experiment2(Leon_Standing_ADS))/Experiment2,T-1100.csv", "w") as f:
   # f.writelines(lines) #write back



# 2nd Commit