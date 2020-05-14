byte var = pow(2,8) - 2;

void setup() {
  Serial.begin(9600);

}

void loop() {
  coolPlot();
  
  delay(100);
}

void printVar(){
  int sizeVar = sizeof(var);

  Serial.print("size of var is ...");
  Serial.println(sizeVar);
  Serial.print("Decimal value of var is ...");
  Serial.println(var);
  Serial.print("Binary value of var is ...");
  Serial.println(var, BIN);
  Serial.print("Hex value of var is ...");
  Serial.println(var, HEX);

  var++;
}

void coolPlot() {
  long cuTime = millis();

  //double sigA = 2*sin(curTime/40);
  //Serial.print(sigA);

  for(int i=0; i<360;i++) {
    double sigC = sin(i*PI/180);
    Serial.println(sigC);
  }
}
