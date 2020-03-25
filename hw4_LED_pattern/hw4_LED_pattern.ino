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
  int val = analogRead(A0) / 4;

  march(val);

  Serial.println(val);

  delay(500);
}

void march(int space) {
  PORTA = 0b00000001;
  delay(space);
  PORTA = 0b00000010;
  delay(space);
  PORTA = 0b00000101;
  delay(space);
  PORTA = 0b00001010;
  delay(space);
  PORTA = 0b00010101;
  delay(space);
  PORTA = 0b00101010;
  delay(space);
  PORTA = 0b01010101;
  delay(space);
  PORTA = 0b10101010;
  delay(space);

  
  PORTA = 0b10101010;
  delay(space);
  PORTA = 0b01010101;
  delay(space);
  PORTA = 0b10101000;
  delay(space);
  PORTA = 0b01010000;
  delay(space);
  PORTA = 0b10100000;
  delay(space);
  PORTA = 0b010000000;
  delay(space);
  PORTA = 0b100000000;
  delay(space);
  PORTA = 0b000000000;
}
