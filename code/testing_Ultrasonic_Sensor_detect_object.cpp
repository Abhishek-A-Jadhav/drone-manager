#include <Arduino.h>
#include <NewPing.h>

#define TRIGGER_PIN  10
#define ECHO_PIN     12
#define MAX_DISTANCE 400

#define LED_PIN      13

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

void setup() {
    Serial.begin(9600);
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);
}

void loop() {
    delay(50);
    int duration = sonar.ping();
    int distance = duration / US_ROUNDTRIP_CM;
    Serial.print(distance);
    Serial.println("cm");

    if (distance <= 10) {
        digitalWrite(LED_PIN, HIGH);
    } else if (distance > 10) {
        digitalWrite(LED_PIN, LOW);
    }
}
