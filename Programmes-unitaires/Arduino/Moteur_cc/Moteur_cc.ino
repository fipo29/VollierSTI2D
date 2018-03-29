

void setup() {
  // put your setup code here, to run once:

  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
}


void loop() {

  // avance
  digitalWrite(2, HIGH);
  digitalWrite(3, LOW);
  delay(5000);

  // arrêt
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  delay(5000);
  
  // recul
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);
  delay(5000)

}

