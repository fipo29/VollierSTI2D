
import serial
import time
ser=serial.Serial('/dev/ttyS0',9600)
ser.close()
while 1:
        ser.open()
        a=300  # (300)10 = (0000 0001 0010 1100)2 = (1)10 (44)10

        pdfaible=a&0xff # on recupere les 8 premiers bits (poid faible) a&255=8 premiers bits: 0010 1100
        pdfort=a>>8&0xff # on decale  à droite les 8 premiers bite et on recupere les 8 poid fort: 0000 0001
        #print(pdfaible)
        #print(pdfort)3
        #print(chr(pdfort))
        #print(chr(pdfaible))
        #print(type(pdfaible))

        ser.write(chr(pdfort))  # on envoi les 8 bits de poid fort
        ser.write(chr(pdfaible)) # on envoi les 8 bits de poid faible

        ser.close()
        time.sleep(3)
