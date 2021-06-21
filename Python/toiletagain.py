

#read the serial data and print it as line
import serial
import time
ser = serial.Serial('/dev/tty.usbmodem14201', baudrate=9600, timeout=.1)

weight = []
counter = 0
f = open("Weightfile", "w")
time.sleep(3)
while counter < 300:
    arduinoData = ser.readline()
    string = arduinoData.decode()  # convert the byte string to a unicode string
    num = str(string)  # convert the unicode string to an int
    print(num)
    weight.append(arduinoData)
    counter += 1

#this is another version
#3rd comment
#4th comment





