


    
###################  client UDP  ###################""

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("192.168.1.101", 5050)
message = str(48)
demande_donnees='1'

try:

    # Send data
    print "envoi message"
    sent = sock.sendto(demande_donnees, server_address)


finally:
    sock.close()