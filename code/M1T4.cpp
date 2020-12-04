#include <Arduino.h>

int soundSensor = 2;
int LED = 13;
boolean LEDStatus = false;

void setup() {
    Serial.begin(9600);
    
    pinMode(soundSensor, INPUT);
    pinMode(LED, OUTPUT);
}

void loop() {

    delay(1);
    
    int SensorData = digitalRead(soundSensor);
    if (SensorData == 1) {
    
        if (LEDStatus == false) {
          LEDStatus = true;
          digitalWrite(LED, HIGH);
        }
        else {
          LEDStatus = false;
          digitalWrite(LED, LOW);
        }
    }
    
    Serial.println(SensorData);
}
