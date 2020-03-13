//    MAE 6194 - Mechatronics
//    Author:   Jonathan Schwartz
//    GWID:     G20740593
//  ===========================================================
//  PATTERN:
//    A trail of four lights will "walk" its way across the LEDS,
//    with each being separated from the adjacent lights by an off
//    LED and progressing along the LEDS. The pattern resets once 
//    all of the lights have traversed all the LEDs=


void setup() {
  DDRA = 0b11111111; //setting all pins to output
  Serial.begin(9600);
}

void loop() {
  int val = analogRead(A0);
  Serial.println(val / 2);
  march(val);
}

void march(int delayTime) {
  
  // Here they come!
  PORTA = 0b00000000;
  delay(delayTime);
  PORTA = 0b00000001;
  delay(delayTime);
  PORTA = 0b00000010;
  delay(delayTime);
  PORTA = 0b00000101;
  delay(delayTime);
  PORTA = 0b00001010;
  delay(delayTime);
  PORTA = 0b00010101;
  delay(delayTime);
  PORTA = 0b00101010;
  delay(delayTime);
  PORTA = 0b01010101;
  delay(delayTime);
  PORTA = 0b10101010;
  delay(delayTime);

  // And there they go. Bye!
  PORTA = 0b01010100;
  delay(delayTime);
  PORTA = 0b10101000;
  delay(delayTime);
  PORTA = 0b01010000;
  delay(delayTime);
  PORTA = 0b10100000;
  delay(delayTime);
  PORTA = 0b01000000;
  delay(delayTime);
  PORTA = 0b10000000;
  delay(delayTime);
}
