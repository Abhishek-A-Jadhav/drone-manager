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
    int duration = sonar.ping();
    int distance = duration / US_ROUNDTRIP_CM;

    digitalWrite(LED_PIN, HIGH);
    delay(distance * 10);
    digitalWrite(LED_PIN, LOW);
    delay(distance * 10);
}
