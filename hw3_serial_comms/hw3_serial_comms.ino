#include <Wire.h>
int val = 0; 

void setup() {
  // put your setup code here, to run once:
  Wire.begin();}

void loop() {
  // put your main code here, to run repeatedly:
  int val = analogRead(A0) / 4;

  
  Wire.beginTransmission(9); // transmit to device #9
  Wire.write(val);              // sends x 
  Wire.endTransmission();    // stop transmitting
  delay(10);
}
