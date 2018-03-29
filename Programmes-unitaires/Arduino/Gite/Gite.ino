int Gite = 0;
void setup() {

  Serial.begin(9600);

}

void loop() {

  Gite = Lecture gite(0); //lecture sur la broche A0
  Serial.print("Gite= "); //Affiche la valeur de la gite
  Serial.println(Gite);

}

int LectureGite(int broche) {
  int gite = analogRead(broche);               //lecture de la valeur de la gite

  if (gite > 340)  gite = gite * 0.5625 - 189; //fonction de tranfert angle=f(mesure)
  else gite = -0.5625 * gite + 189;
  return gite;                                 //retourne la valeur de la gite

}
