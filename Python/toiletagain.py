

#read the serial data and print it as line
import serial
import time
import os


ser = serial.Serial('/dev/tty.usbmodem14201', baudrate=9600, timeout=.1)

weight = [5]
counter = 0
f = open("Exp4,T-7.csv", "w")
time.sleep(4)
while counter < 100:
    arduinoData = ser.readline()
    string = arduinoData.decode()  # convert the byte string to a unicode string
    num = str(string)  # convert the unicode string to an int
    print(num)
    weight.append(num)
    f.write(str(num))
    f.write(str("\n"))
    counter += 1
From1 = "/Users/Leon/Documents/ToiletProjectUni2021/Python/Exp4,T-7.csv"
To1 = "/Users/Leon/Documents/ToiletProjectUni2021/Exp4(Leon_Standing_ADS)/Exp4,T-7.csv"
os.rename(From1,To1)


#with open("/Users/Leon/Documents/ToiletProjectUni2021/Experiment2(Leon_Standing_ADS)/Experiment2,T-700.csv") as f:
 #   lines = f.readlines()  # read
#lines[0] = ("0.0" + "\n")  # you can replace zero with any line number
#with open("/Users/Leon/Documents/ToiletProjectUni2021/Experiment2(Leon_Standing_ADS))/Experiment2,T-700.csv", "w") as f:
   # f.writelines(lines) #write back



# 2nd Commit