
int broche = 1;
int OrVent = 0;


void setup() {
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  OrVent = LectureOrVent(broche);
  Serial.print("Orientation du vent en °: ");
  Serial.println(OrVent);

}


int LectureOrVent(int Broche) {
  int angle = 0;
  int val = analogRead(Broche);
  if (val > 512) angle = -(val) * 0.3516 + 360;
  else angle = val * 0.3516;
  return angle;

}
