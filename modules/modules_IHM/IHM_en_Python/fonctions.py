#Import ce fichier dans tous les fichiers venant de Qt
#import fonctions

#module A
metier = ''
#métier de l'utilisateur (patient ou médecin)

#module B
identifiant = ''
#identifiant de l'utilisateur
motdepass = ''
#motdepass de l'utilisateur
coins = ''

#module C
loc = ''
#localisation du rendez-vous
typepraticien = ''
#type de praticien demandé
typeRdV = ''
#type de Rendez-Vous demandé
dateRdV = ''
#date du rendez-Vous

#module D
nomdudoc = ''
#Nom du docteur
horairerdv = ''
#Horaire du Rendez-Vous
Info = ''
#Informations supplémentaires pour le docteur

mugi = False

def continu(bool):
    global mugi
    mugi = bool

def continus():
    return mugi

PInom = ''
PIprenom = ''
PIjour = ''
PImois = ''
PIannee = ''
PInumero = ''



def finom(texte):
    global PInom
    PInom = texte

def fiprenom(texte):
    global PIprenom
    PIprenom = texte

def fijour(texte):
    global PIjour
    PIjour = texte

def fimois(texte):
    global PImois
    PImois = texte

def fiannee(texte):
    global PIannee
    PIannee = texte

def finumero(texte):
    global PInumero
    PInumero = texte

DIville = ''
DIadresse = ''
DIcodepostal = ''

def fiville(texte):
    global DIville
    DIville = texte

def fiadresse(texte):
    global DIadresse
    DIadresse = texte

def ficodepostale(texte):
    global DIcodepostal
    DIcodepostal = texte


def Inom():
    return PInom

def Iprenom():
    return PIprenom

def Ijour():
    return PIjour

def Imois():
    return PImois

def Iannee():
    return PIannee

def Inumero():
    return PInumero

def Iville():
    return DIville

def Iadresse():
    return DIadresse

def Icodepostal():
    return DIcodepostal

def affiche(texte):
    global metier
    metier = texte

def verificationId(texte):
    global identifiant
    identifiant = texte

def verificationMdP(texte):
    global motdepass
    motdepass = texte

def con_ins(bool):
    global coins
    coins = bool

def location(texte):
    global loc
    loc = texte

def praticien(texte):
    global typepraticien
    typepraticien = texte

def Rdv(texte):
    global typeRdV
    typeRdV = texte

def date(texte):
    global dateRdV
    dateRdV = texte

def medecin(texte):
    global nomdudoc
    nomdudoc = texte

def horaire(texte):
    global horairerdv
    horairerdv = texte

def infodoc(texte):
    global Info
    Info = texte

def imprime(texte):
    print(texte)

def connection(commande):
    global n 
    n = commande

def Ametier():
    return metier
    
def Bidentifiant():
    return identifiant

def Bmotdepass():
    return motdepass

def Bcreationcompte():
    return coins

def Clocation():
    return loc

def Cpraticien():
    return typepraticien

def CRdV():
    return typeRdV

def Cjour():
    return PIjour

def Cmois():
    return PImois

def Cannee():
    return PIannee

def Ddocname():
    return nomdudoc

def DHoraireRdv():
    return horairerdv

def DInfos():
    return Info