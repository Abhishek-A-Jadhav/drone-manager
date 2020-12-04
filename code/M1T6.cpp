#include <Arduino.h>
#include <Servo.h>
#include <NewPing.h>


#define TrigPin     6
#define EchoPin     7
#define MaxDistance 400

#define ESCPin      10
#define distanceMin 6
#define distanceMax 25
#define speedMin    1300
#define speedMax    1380

Servo ESC;

NewPing sonar(TrigPin, EchoPin, MaxDistance);

void setup() {

    Serial.begin(9600);
    ESC.attach(ESCPin);

}

void loop() {

    float duration = sonar.ping();

    float distance = duration / US_ROUNDTRIP_CM;

    int speed = map(distance, distanceMin, distanceMax, speedMin, speedMax);
    
    if (distance <= distanceMax) {
        ESC.writeMicroseconds(speed);
    } else if (distance > distanceMax || distance < distanceMin) {
        ESC.writeMicroseconds(0);
    }

}