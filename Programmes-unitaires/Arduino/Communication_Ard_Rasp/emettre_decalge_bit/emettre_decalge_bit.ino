void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {

  int a = 300;    // on veut envoyer le chiffre 300
  byte tableau[2];
  byte byteLow = a & 0xff; // on recupere les 8 bits de poid faible
  byte byteHigh = a>>8 & 0xff; // on decale à droite pour recuperer les 8 bits de poid fort
  tableau[0]=byteLow;
  tableau[1]=byteHigh;
  Serial.write(tableau,2);

  delay(5000);
}
