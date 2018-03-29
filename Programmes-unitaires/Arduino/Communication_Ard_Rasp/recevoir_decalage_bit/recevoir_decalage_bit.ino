
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);

}

void loop() { // run over and over

  int buffers = 0;
  long buffers2 = 0;
  while ( int len = mySerial.available()) {

    Serial.println(len);
    for (int i = 1; i < 3; i++ ) { // boucle de 1 à 2 pour lecture de 2 octets
      buffers = mySerial.read();  // lecture du premier octet


      buffers2 = buffers2 | buffers; // on fait un ou entre loctet reçu et le buffer de stockage


      if (i < 2) {              // si ce n est pas le dernier octet: on decale a gauche pour recuperer la suite
        buffers2 = buffers2 << 8;
      }
      else {                    // sinon, dernier octet: on affiche
        Serial.println(buffers2);
        break;      // on sort du while quand octet transmit
      }
    }
  }
}

