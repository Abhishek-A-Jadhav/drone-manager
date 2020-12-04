#include <Wire.h>
#include <MPU6050_tockn.h>
#include <Servo.h>

MPU6050 mpu6050(Wire);
Servo ESC1, ESC2;

float elapsedTime, timePrev, time;

float PID, pwm1, pwm2, error, previousError;
float pid_p = 0;
float pid_i = 0;
float pid_d = 0;

double kp = 1;
double ki = 0.008;
double kd = 0.7;

double throttle1 = 1430;
double throttle2 = 1345;
double speedMin = 1325;
double speedMax = 1500;
float desiredAngle = 0;

void setup() {

    Serial.begin(9600);
    Wire.begin();

    mpu6050.begin();
    mpu6050.calcGyroOffsets(true);

    ESC1.attach(10);
    ESC2.attach(9);

    time = millis();

    ESC1.writeMicroseconds(1000); 
    ESC2.writeMicroseconds(1000);
    delay(8000);

}

void loop() {

    timePrev = time;
    time = millis();
    elapsedTime = (time - timePrev) / 1000;

    mpu6050.update();

    float angle = mpu6050.getAngleY();

    error = angle - desiredAngle;

    pid_p = kp*error;
    if(-10 < error < 10) {
        pid_i = pid_i+(ki*error);  
    }
    pid_d = kd*((error - previousError)/elapsedTime);

    PID = pid_p + pid_i + pid_d;

    if(PID < -1000) {
        PID = -1000;
    }
    if(PID > 1000) {
        PID = 1000;
    }

    pwm1 = throttle1 + PID;
    pwm2 = throttle2 - PID;

    if(pwm1 < speedMin) {
        pwm1 = speedMin;
    }
    if(pwm1 > speedMax) {
        pwm1 = speedMax;
    }

    if(pwm2 < speedMin) {
        pwm2 = speedMin;
    }
    if(pwm2 > speedMax) {
        pwm2 = speedMax;
    }

    if (angle > (desiredAngle - 1) && angle < (desiredAngle + 1)) {
        pwm1 = pwm2 + 85;
        Serial.println("Stable");
    }

    ESC1.writeMicroseconds(pwm1);
    ESC2.writeMicroseconds(pwm2);
    previousError = error;

    Serial.print("1: ");
    Serial.print(pwm1);
    Serial.print("\t2: ");
    Serial.print(pwm2);
    Serial.print("\tangle: ");
    Serial.println(angle);

}