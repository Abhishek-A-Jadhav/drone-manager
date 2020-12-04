import serial
import time

ser = serial.Serial("COM3", 9600)

while True:
    inp = input("State: ")

    if inp == '1':
        ser.write(inp.encode())
    elif inp == '0':
        ser.write(inp.encode())
