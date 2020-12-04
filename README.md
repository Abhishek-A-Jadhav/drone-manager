# drone-manager

---
This is version 1.0 of Drone Manager. This is a project I am working on to create controllers for a drone using various sensors. Since it is way cheaper than a _transmitter & receiver_ and also gives us ability to make the drone an autonomous system.

It is an interfacing tool which calls a bunch of functions to interact with the drone. Requires an arduino to work.

**Known bugs:** Not able to set the port directly (User has to set it manually inside the `main.py` file).

Please report any other bugs on abhishekajadhavb4@gmail.com I will surely try and fix them in next version.

---
### Usage:

**Just run `main.py` through the terminal. Make sure to have `kivy` installed on your device. Created and tested on Linux. Works on Windows, Mac & Linux.**

### Requirements:
1. Arduino
2. IMU MPU6050
3. Jumper Wires
4. Bread Board
5. Ultrasonic Sensor HC-SR04
6. Sound Detection Sensor
7. Li Po Battery
8. Bluetooth Module HC-05
9. DC Motor
10. Soldering Iron Kit

### Layout of the interface:
It is divided in **four** main parts. Each part has its own number of tasks which will get you ready for the next phase.

- Preparation Phase I
- On Ground Test
- Preparation Phase II
- In Air Test

To complete the project (i.e. to get the drone in air and have fun with it), all the **four** parts are to be completed in serial order. The tasks in these parts are designed in such a way that upon completion on one task you will get understanding of the things needed for next task (thus, in serial order).

<p align = "center">
<br />
<b>A test stand will be required to complete the first two parts</b>

<br />
<br />
<br />

<img src = "code/ignoreThisFile.png" width = "500">
</p>
<br />

On going into any of the **four** parts, a list of tasks is available to choose from. Inside every task there is a button to copy the `python` and `arduino` code for that task. On clicking this button the code will be copied to the clipboard and can be used to upload it on the arduino.\
There are few tasks which does not require any interface. In such case only buttons for copying the code is available.

**In the current version of this tool, only `Preparation Phase I` and `On Ground` parts are available. I am still working on the next stages of this project. And will be updated as soon as they are ready.**

---
