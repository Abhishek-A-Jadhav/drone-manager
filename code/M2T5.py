import serial
import time

ser = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1)

# print("")
# print("-------------------Script Starting--------------------")

# for i in range(15, 0, -1):
#     print(i)
#     time.sleep(1)

# print("-------------------Script Started--------------------")
# print("")

while True:
    # state = str(1)
    state = input("State: ")
    ser.write(state.encode())
    print(state)