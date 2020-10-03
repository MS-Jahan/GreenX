Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import serial
import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig=plt.figure()
 
 
i=0
x=list()
y=list()
i=0
ser = serial.Serial('COM13',9600)
ser.close()
ser.open()
while True:
 
    data = ser.readline()
    print(data.decode())
    x.append(i)
    y.append(data.decode())
 
    plt.scatter(i, float(data.decode()))
    i += 1
    plt.show()
    plt.pause(0.0001)