
####################  interface  #################
from Tkinter import *
###################  client UDP  ###################""
import socket


###############################################################################################################
#################           Methodes de MAJ des valeurs  et communication  avec le serveur     ################
###############################################################################################################

def majbome(nouvelleValeur): # Envoie de la commande moteur pour la bome
    # nouvelle valeur en argument
    EnvoiOrdre(nouvelleValeur,"2")

def majgouvernail(nouvelleValeur): # Envoie de la commande moteur pour le gouvernail
    # nouvelle valeur en argument
    EnvoiOrdre(nouvelleValeur,"1")



def EnvoiOrdre(nouvelleValeur,NMoteur):
    try:



    finally:
        sock.close()

###################################################################################################################
##########################################   Conception interface  ################################################
###################################################################################################################


# Construction de la fenetre principale "interface"
interface = Tk()

interface.title('Interface Voilier')

#Creation des variable interactive (mise a jour automatique)
ValeurBome = StringVar()
ValeurBome.set(0)
ValeurGouvernail = StringVar()
ValeurGouvernail.set(0)
gite=StringVar()
gite.set(0)
Lat=StringVar()
Lat.set(0)
Long=StringVar()
Long.set(0)
OrVent=StringVar()
OrVent.set(0)
VitVent=StringVar()
VitVent.set(0)
trameMoteur=bytearray(["1",0,0])

# Configuration du gestionnaire de grille
interface.rowconfigure(4, weight=1)
interface.columnconfigure(6, weight=1)

#######################"   Conception des boutton et des labels"##########################################
# Construction bouton "Quitter"
qb = Button(interface, text='Quitter', command=interface.quit)


#label Gite
FrameGiteLabel = Frame(interface,borderwidth=2,relief=GROOVE)
chaine1="Gite bateau:"
Label(FrameGiteLabel,text=chaine1).pack(padx=10,pady=10)

#valeur Gite
FrameGiteValeur = Frame(interface,borderwidth=2,relief=GROOVE)
Label(FrameGiteValeur,textvariable=gite).pack(padx=10,pady=10)

#label Orientation vent
FrameOrVentLabel = Frame(interface,borderwidth=2,relief=GROOVE)
chaine2="Orientation du vent:"
Label(FrameOrVentLabel,text=chaine2).pack(padx=10,pady=10)

#Valeur Orientation vent
FrameOrVentValeur = Frame(interface,borderwidth=2,relief=GROOVE)
Label(FrameOrVentValeur,textvariable=OrVent).pack(padx=10,pady=10)

#label Vitesse du vent
FrameVitVentLabel = Frame(interface,borderwidth=2,relief=GROOVE)
chaine3="Vitesse du vent:"
Label(FrameVitVentLabel,text=chaine3).pack(padx=10,pady=10)

#Valeur Vitesse du vent
FrameVitVentValeur = Frame(interface,borderwidth=2,relief=GROOVE)
Label(FrameVitVentValeur,textvariable=VitVent).pack(padx=10,pady=10)

#Label Latitude
FrameLatLabel = Frame(interface,borderwidth=2,relief=GROOVE)
chaine4="Latitude:"
Label(FrameLatLabel,text=chaine4).pack(padx=10,pady=10)

#Valeur Latitude
FrameLatValeur = Frame(interface,borderwidth=2,relief=GROOVE)
Label(FrameLatValeur,textvariable=Lat).pack(padx=10,pady=10)

#Label Longitude
FrameLongLabel = Frame(interface,borderwidth=2,relief=GROOVE)
chaine5="Longitude:"
Label(FrameLongLabel,text=chaine5).pack(padx=10,pady=10)

#Valeur Longitude
FrameLongValeur = Frame(interface,borderwidth=2,relief=GROOVE)
Label(FrameLongValeur,textvariable=Long).pack(padx=10,pady=10)

# Creation d'un widget Scale Bome
echelleBome = Scale(interface,from_=-90,to=90,resolution=1,orient=HORIZONTAL,\
length=300,width=20,label="Bome",tickinterval=10,variable=ValeurBome,command=majbome)


# Creation d'un widget Scale
echelleGouv = Scale(interface,from_=-90,to=90,resolution=1,orient=HORIZONTAL,\
length=300,width=20,label="Gouvernail",tickinterval=10,variable=ValeurGouvernail,command=majgouvernail)

#######################"   FIN  Conception des boutton et des labels"##########################################



# Placement du bouton dans "interface"
qb.grid(row=0, column=0, sticky="nsew")


FrameGiteLabel.grid(row=1, column=0,sticky="nsew")
FrameGiteValeur.grid(row=1, column=1,sticky="nsew")

FrameOrVentLabel.grid(row=1, column=2,sticky="nsew")
FrameOrVentValeur.grid(row=1, column=3,sticky="nsew")

FrameVitVentLabel.grid(row=1, column=4,sticky="nsew")
FrameVitVentValeur.grid(row=1, column=5,sticky="nsew")

FrameLatLabel.grid(row=2, column=0,sticky="nsew")
FrameLatValeur.grid(row=2, column=1,sticky="nsew")

FrameLongLabel.grid(row=2, column=2,sticky="nsew")
FrameLongValeur.grid(row=2, column=3,sticky="nsew")

echelleBome.grid(row=3,column=0,sticky="nsew")

echelleGouv.grid(row=3,column=2,sticky="nsew")


# Lancement de la "boucle principale"
interface.mainloop()

###################################################################################################################
#########################################  FIN Conception interface  ##############################################
###################################################################################################################