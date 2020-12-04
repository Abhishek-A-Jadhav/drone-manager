#include <Servo.h>
#include <PID_Tuning.h>

PID pid = PID(1.1, 0.01, 0.8);

Servo ESC1, ESC2;

String desiredAngle = "0";

void setup() {

    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);

    pid.begin();

    ESC1.attach(10);
    ESC2.attach(9);

    ESC1.writeMicroseconds(1000); 
    ESC2.writeMicroseconds(1000);
    delay(8000);

}

void loop() {

    if (Serial.available() > 0) {
        desiredAngle = Serial.readString();
    }

    int num = desiredAngle.toInt();

    pid.tune(num);

    int pwm1 = pid.getPwm1();
    int pwm2 = pid.getPwm2();

    if (pid.getAngleY() == num) {
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }

    ESC1.writeMicroseconds(pwm1);
    ESC2.writeMicroseconds(pwm2);

    Serial.print("1: ");
    Serial.print(pwm1);
    Serial.print("\t2: ");
    Serial.print(pwm2);
    Serial.print("\tangleY: ");
    Serial.print(pid.getAngleY());
    Serial.print("\tdesiredAngle: ");
    Serial.println(num);

}