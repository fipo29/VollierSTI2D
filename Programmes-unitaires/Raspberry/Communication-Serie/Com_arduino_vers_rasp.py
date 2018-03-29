import serial
ser=serial.Serial('/dev/ttyS0',9600)
ser.close()
while 1:
        if ser:
                ser.open()
                info=ser.read(2)        #lecture de 2 octets
                #print(long(ord(info[0])))

                Pdfaible=long(ord(info[0])) # convertion de str en byte
                Pdfort=long(ord(info[1]))

                print("Poid fort: %d" % Pdfort)
                print("Poid faible: %d" % Pdfaible)

                resultat=Pdfort<<8              #decalage de 8 bits vers la gauche
                resultat=resultat | Pdfaible    #concatenation octet fort et faible par un ou logique
                print("concatetnation %d" % resultat)

                print("_____")
                ser.close()

        else:
                print("pas de transmission")

