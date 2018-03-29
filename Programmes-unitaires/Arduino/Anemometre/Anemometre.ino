int Vitesse;
int i = 0;
int broche=2; // capteur sur la broche numérique 2

void setup() {

  Serial.begin(9600);
  pinMode(2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Vitesse = LectureVitVent(broche);
  Serial.print("Vitesse du vent en m/s: ");
  Serial.println(Vitesse);

}

float LectureVitVent(int Broche) {

  float vitesse;
  float perimetre = 2 * 3.14 * 0.06; //rayon = 0.06 m
  float tempHaut = pulseIn(Broche, LOW);
  float tempBas = pulseIn(Broche, HIGH);
  float duree = (tempHaut + tempBas) * 0.000001; //duree en s

  if (tempHaut > 0 & tempBas > 0) {
    vitesse = (perimetre / duree);
    return vitesse;
  }
  else return 0;
}

