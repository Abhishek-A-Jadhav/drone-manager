#include <Arduino.h>
#include <Servo.h>


Servo ESC1, ESC2;

String speed = "0";

void setup() {

    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);

    ESC1.attach(10);
    ESC2.attach(9);

    ESC1.writeMicroseconds(1000); 
    ESC2.writeMicroseconds(1000);
    delay(8000);

}

void loop() {

    if (Serial.available() > 0) {
        speed = Serial.readString();
    }

    int num = speed.toInt();

    ESC1.writeMicroseconds(num);
    ESC2.writeMicroseconds(1365);

}