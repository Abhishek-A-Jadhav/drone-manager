#include <Arduino.h>

int LED = 13;
int inp = 0;

void setup() {
    pinMode(LED, OUTPUT);
    
    Serial.begin(9600);
    Serial.print("State: ");

    digitalWrite(LED, LOW);
}

void loop() {

    if (Serial.available() > 0) {
        inp = Serial.read();
    }

    if (inp == '1') {
        digitalWrite(LED, HIGH);
    }

    if (inp == '0') {
        digitalWrite(LED, LOW);
    }
}
