#include <Arduino.h>
#include <Servo.h>
#include <NewPing.h>


#define TrigPin1    6
#define EchoPin1    7
#define TrigPin2    5
#define EchoPin2    8
#define MaxDistance 400

#define ESC1Pin     10
#define ESC2Pin     9
#define distanceMin 6
#define distanceMax 25
#define speedMin    1300
#define speedMax    1380
#define speedDiff   85
#define absVal      2

Servo ESC1, ESC2;

NewPing sonar1(TrigPin1, EchoPin1, MaxDistance);
NewPing sonar2(TrigPin2, EchoPin2, MaxDistance);

void setup() {

    Serial.begin(9600);

    ESC1.attach(ESC1Pin);
    ESC2.attach(ESC2Pin);

}

void loop() {

    float duration1 = sonar1.ping();
    float duration2 = sonar2.ping();

    float distance1 = duration1 / US_ROUNDTRIP_CM;
    float distance2 = duration2 / US_ROUNDTRIP_CM;

    int speed1 = map(distance1, distanceMin, distanceMax, speedMin, speedMax);
    int speed2 = map(distance2, distanceMin, distanceMax, speedMin, speedMax);

    if (abs(distance1 - distance2) <= absVal) {
        speed1 = (speed1+speed2) / absVal;
        speed2 = (speed1+speed2) / absVal;
    }
    
    if (distance1 <= distanceMax && distance2 <= distanceMax) {
        ESC1.writeMicroseconds(speed1 + speedDiff);
        ESC2.writeMicroseconds(speed2);
    } if (distance1 > distanceMax || distance2 > distanceMax) {
        ESC1.writeMicroseconds(0);
        ESC2.writeMicroseconds(0);
    } if (distance1 < distanceMin) {
        ESC1.writeMicroseconds(0);
    } if (distance2 < distanceMin) {
        ESC2.writeMicroseconds(0);
    } else if (distance1 < distanceMin && distance2 < distanceMin) {
        ESC1.writeMicroseconds(0);
        ESC2.writeMicroseconds(0);
    }

//    Serial.print("Distance 1: ");
//    Serial.print(distance1);
//    Serial.println(" cm");
//    Serial.print("Speed1: ");
//    Serial.println(speed1);

//    Serial.println("");

//    Serial.print("Distance 2: ");
//    Serial.print(distance2);
//    Serial.println(" cm");
//    Serial.print("Speed2: ");
//    Serial.println(speed2);

//    Serial.println("");

//    delay(1000);

}