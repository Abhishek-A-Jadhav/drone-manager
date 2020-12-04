#include <Arduino.h>
#include <Servo.h>

Servo ESC1, ESC2;

int speed = 0;

void setup() {

    Serial.begin(9600);
    
    ESC1.attach(10);
    ESC2.attach(9);

    ESC1.writeMicroseconds(1200);
    delay(3000);
    ESC2.writeMicroseconds(1200);
    delay(5000);

}

void loop() {

    if (Serial.available() > 0) {
        speed = Serial.parseInt();
    }

    ESC1.writeMicroseconds(speed + 85);
    ESC2.writeMicroseconds(speed);

    Serial.println(speed);

}
