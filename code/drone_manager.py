import serial
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.core.window import Window
import pyperclip as pc
import numpy as np
import cv2
import imutils
from scipy.interpolate import interp1d
import time

Window.size = (1920, 1080)
Window.clearcolor = (0.1, 0.1, 0.1, 1)

# -------------------SET PORT-------------------
port = "/dev/ttyACM0"       # COM3, /dev/ttyACM0
# ----------------------------------------------

# ser = serial.Serial(port, baudrate=9600, timeout=1)

class Window1(Screen):
    pass


class Window2(Screen):
    pass


class Main1(Screen):
    pass


class Main2(Screen):
    pass


class Main3(Screen):
    pass


class Main4(Screen):
    pass


class Main1_Task1(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M1T1.cpp')
        pc.copy(arduinoCode.read())


class Main1_Task2(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M1T2.cpp')
        pc.copy(arduinoCode.read())


class Main1_Task3(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M1T3.cpp')
        pc.copy(arduinoCode.read())

    def pythonCopy(self):
        pythonCode = open('M1T3.py')
        pc.copy(pythonCode.read())


class Main1_Task4(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M1T4.cpp')
        pc.copy(arduinoCode.read())


class Main1_Task5(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M1T5.cpp')
        pc.copy(arduinoCode.read())


class Main1_Task6(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M1T6.cpp')
        pc.copy(arduinoCode.read())


class Main2_Task1(Screen):
    def arduinoCopy(self):
        arduinoCode = open('M2T1.cpp')
        pc.copy(arduinoCode.read())


class Main2_Task2(Screen):
    pass


class Main2_Task3(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M2T3.cpp')
        pc.copy(arduinoCode.read())


class Main2_Task4(Screen):
    pass


class Main2_Task5(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M2T5.cpp')
        pc.copy(arduinoCode.read())

    def pythonCopy(self):
        pythonCode = open('M2T5.py')
        pc.copy(pythonCode.read())


class Main2_Task6(Screen):

    def arduinoCopy(self):
        arduinoCode = open('M2T6.cpp')
        pc.copy(arduinoCode.read())

    def pythonCopy(self):
        pythonCode = open('M2T6.py')
        pc.copy(pythonCode.read())
    
    def pattern1(self):
        
        speed = 1460
        ser.write(speed.encode())
        for i in range(5):
            time.sleep(1)

        speed = 1440
        ser.write(speed.encode())
        for i in range(5):
            time.sleep(1)

    
    def pattern2(self):
        
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

    def stop(self):
        speed = 1450
        ser.write(speed.encode())


class Main2_Task7(Screen):
    
    def arduinoCopy(self):
        arduinoCode = open('M2T7.cpp')
        pc.copy(arduinoCode.read())

    def pythonCopy(self):
        pythonCode = open('M2T7.py')
        pc.copy(pythonCode.read())
    
    def writeAngle(self):
        writeAngle = self.ids.writeAngle.text
        ser.write(writeAngle.encode())
        self.ids.confirmationAngle.text = writeAngle

        if (len(writeAngle) == 0):
            self.ids.confirmationAngle.text = "0"
        elif (int(writeAngle) > 40 or int(writeAngle) < -40):
            self.ids.errorAngle.text = "Given angle is out of range"
            self.ids.confirmationAngle.text = "0"
            ser.write("0".encode())
        else:
            self.ids.errorAngle.text = ""

    def reset(self):
        self.ids.writeAngle.text = ""
        self.ids.confirmationAngle.text = "0"
        self.ids.errorAngle.text = ""
        ser.write("0".encode())


class Main2_Task8(Screen):

    def arduinoCopy(self):
        arduinoCode = open('M2T8.cpp')
        pc.copy(arduinoCode.read())

    def pythonCopy(self):
        pythonCode = open('M2T8.py')
        pc.copy(pythonCode.read())
    
    def run(self):

        cap = cv2.VideoCapture(0)

        prevX = 0
        while(True):
            
            try:
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                h = self.ids.h.text
                s = self.ids.s.text
                v = self.ids.v.text

                m1 = np.array([int(h), int(s), int(v)]) # [0, 64, 162]
                m2 = np.array([255, 255, 255])

                mask = cv2.inRange(hsv, m1, m2)

                countours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                countours = imutils.grab_contours(countours)

                area = 0
                x = y = 0
                center = "0"

                for c in countours:
                    area = cv2.contourArea(c)

                    if area > 1000:

                        moments = cv2.moments(c)

                        x = int(moments["m10"] / moments["m00"])
                        y = int(moments["m01"] / moments["m00"])

                        center = "Center: " + str(x) + "," + str(y)
                        area = "Area: " + str(area)

                        cv2.circle(frame, (x, y), 6, (0, 0, 0), -1)
                        cv2.putText(frame, center, (x-140, y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (45, 45, 45), 2)
                        cv2.putText(frame, area, (x-140, y-45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (45, 45, 45), 2)

                    cv2.imshow("frame", frame)

                # print(f"Location: {center}")

            # -------------------------------------------------------------------------------------------------------
                # x range: (15, 625)
                # Left: 1490, Middle: 1450, Right: 1410
                diff = x - prevX

                if abs(diff) > 3:
                    mapVal = interp1d([625, 15], [1410, 1490])
                    speed = int(mapVal(x))
                else:
                    speed = 1450

                ser.write(speed.encode())
                print(speed)

                prevX = x

            # -------------------------------------------------------------------------------------------------------
                if cv2.waitKey(1) == ord('q'):
                    break

            except ValueError:
                continue

        cap.release()
        cv2.destroyAllWindows()

    def reset(self):
        self.ids.h.text = ""
        self.ids.s.text = ""
        self.ids.v.text = ""


class Main3_Task1(Screen):
    pass


class Main3_Task2(Screen):
    pass


class Main4_Task1(Screen):
    pass


class Main4_Task2(Screen):
    pass


class Main4_Task3(Screen):
    pass


class Main4_Task4(Screen):
    pass


class Main4_Task5(Screen):
    pass


class Main4_Task6(Screen):
    pass


class Main4_Task7(Screen):
    pass


class Main4_Task8(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


windows = Builder.load_file("drone_manager.kv")


class DroneManagingApp(App):
    def build(self):
        # return Window1()
        return windows


if __name__ == "__main__":
    DroneManagingApp().run()