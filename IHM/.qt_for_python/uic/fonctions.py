#Import ce fichier dans tous les fichiers venant de Qt
#import fonctions

metier = ''
n = 0

def affiche(texte):
    global metier
    metier = texte

def imprime(texte):
    print(texte)

def connection(commande):
    global n 
    n = commande
    








"""
        self.PatientButton.released.connect(lambda: fonctions.affiche("Patient"))
        self.DoctorButton.released.connect(lambda: fonctions.affiche("Doctor"))

        self.B_Retour_commandLinkButton.released.connect(lambda: fonctions.connection("back")) 
"""