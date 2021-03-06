//    MAE 6194 - Mechatronics
//    Author:   Jonathan Schwartz
//    GWID:     G20740593
//  ===========================================================
//  Potentiometer Glow:
//    Adjusting the potentiometer (value read in through pin A0)
//    results in the lights glowing at different brightnesses

const int pins[] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup() {
  DDRA = 0b11111111; //setting all pins to output
  Serial.begin(9600);
}

void loop() {
  int val = analogRead(A0) / 4;
  int pin_count = sizeof(pins) / sizeof(pins[0]);
  
  for (int i=2;i<(pin_count + 2);i++) {
    analogWrite(i, val);
  }

  Serial.println(val);

  delay(100);
}
