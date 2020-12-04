#include <Arduino.h>
#include <NewPing.h>

#define TrigPin1    6
#define EchoPin1    7
#define TrigPin2    5
#define EchoPin2    8
#define MaxDistance 400

NewPing sonar1(TrigPin1, EchoPin1, MaxDistance);
NewPing sonar2(TrigPin2, EchoPin2, MaxDistance);

void setup() {

    Serial.begin(9600);
    
}

void loop() {

    int distance1 = sonar1.ping_cm();
    int distance2 = sonar2.ping_cm();

    Serial.print("Distance 1: ");
    Serial.print(distance1);
    Serial.println(" cm");

    Serial.println("");

    Serial.print("Distance 2: ");
    Serial.print(distance2);
    Serial.println(" cm");

    delay(500);

}