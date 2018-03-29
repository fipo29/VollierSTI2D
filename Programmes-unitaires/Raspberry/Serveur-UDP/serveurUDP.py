
##################### serveur UDP  ############################""
import socket
##################### Communication serie  ######################
import serial
ser=serial.Serial('/dev/ttyACM0',9600)



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ("192.168.0.23", 5050)
sock.bind(server_address)


while True:

        #Reception des donnees de l interface (commande moteur)
        data, address = sock.recvfrom(1024)


        #Si il y a de la data:
        if data:

            print data
            datagram = bytearray(data)
            print str(datagram[0]),str(datagram[1]),str(datagram[2]),str(datagram[3]),str(datagram[4])
   
    