#include <NewPing.h>
 
#define TRIGGER_PIN 2
#define ECHO_PIN 3
#define MAX_DISTANCE 20

// NewPing setup of pins and maximum distance
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); 
 
void setup() {
   Serial.begin(9600);
}
 
void loop() {
   delay(50);
   unsigned int distance = sonar.ping_cm();
   Serial.print(distance);
   Serial.println("cm"); 
   }