import serial
import time

port = "/dev/ttyACM0"
ser = serial.Serial(port, baudrate=9600, timeout=1)

# Pattern 1
speed = 1460
ser.write(speed.encode())
for i in range(5):
    time.sleep(1)

speed = 1440
ser.write(speed.encode())
for i in range(5):
    time.sleep(1)

# Pattern 2
speed = 1455
ser.write(speed.encode())
for i in range(5):
    time.sleep(1)

speed = 1460
ser.write(speed.encode())
for i in range(3):
    time.sleep(1)

speed = 1440
ser.write(speed.encode())
for i in range(3):
    time.sleep(1)

speed = 1445
ser.write(speed.encode())
for i in range(5):
    time.sleep(1)