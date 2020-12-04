import numpy as np
import cv2
import imutils
import serial
from scipy.interpolate import interp1d

# ser = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1)

def doNothing(x):
    pass

cap = cv2.VideoCapture(0)

# cv2.namedWindow("settings")
# cv2.createTrackbar("LH", "settings", 0, 255, doNothing)
# cv2.createTrackbar("LS", "settings", 0, 255, doNothing)
# cv2.createTrackbar("LV", "settings", 0, 255, doNothing)
# cv2.createTrackbar("UH", "settings", 0, 255, doNothing)
# cv2.createTrackbar("US", "settings", 0, 255, doNothing)
# cv2.createTrackbar("UV", "settings", 0, 255, doNothing)

x = 0

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lh = cv2.getTrackbarPos("LH", "settings")
    # ls = cv2.getTrackbarPos("LS", "settings")
    # lv = cv2.getTrackbarPos("LV", "settings")
    # uh = cv2.getTrackbarPos("UH", "settings")
    # us = cv2.getTrackbarPos("US", "settings")
    # uv = cv2.getTrackbarPos("UV", "settings")

    m1 = np.array([0, 64, 162])
    m2 = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, m1, m2)

    # result = cv2.bitwise_and(frame, frame, mask=mask)

    countours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countours = imutils.grab_contours(countours)

    area = 0
    x = y = 0
    center = "0"

    for c in countours:
        area = cv2.contourArea(c)

        if area > 1000:
            # cv2.drawContours(frame, [c], -1, (192, 130, 76), 2)

            moments = cv2.moments(c)

            x = int(moments["m10"] / moments["m00"])
            y = int(moments["m01"] / moments["m00"])

            center = "Center: " + str(x) + "," + str(y)
            area = "Area: " + str(area)

            cv2.circle(frame, (x, y), 6, (0, 0, 0), -1)
            cv2.putText(frame, center, (x-140, y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (45, 45, 45), 2)
            cv2.putText(frame, area, (x-140, y-45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (45, 45, 45), 2)

        cv2.imshow("frame", frame)

    print(f"Location: {center}")

# -------------------------------------------------------------------------------------------------------
    # x range: (15, 625)
    # Left: 1490, Middle: 1450, Right: 1410
    diff = x - prevX

    if abs(diff) > 10:
        speed = interp1d([625, 15], [1410, 1490])
    else:
        speed = 1450

    # ser.write(speed.encode())

    prevX = x

# -------------------------------------------------------------------------------------------------------
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()