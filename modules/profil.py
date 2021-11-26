MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"]

class Profil:
    """Les parametres communs à tous les profils sont le prenom le nom le mail, 
    telephone et adresse, on rajoutera des choses pour le docteur/patient"""
    
    def __init__(self):
        self.prenom = "" #STR
        self.nom = "" #STR
        self.mail = "" #STR
        self.telephone = 0 #INT
        self.adresse = "" #STR

    def saisie(self, prenom, nom, mail, telephone, adresse):
        self.prenom = str(prenom) #STR
        self.nom = str(nom) #STR
        self.mail = str(mail) #STR
        self.telephone = str(telephone) #STR
        self.adresse = str(adresse) #STR
        

class Docteur(Profil):
    """Le docteur prends en plus en parametre de lui meme son metier 
    ie si c'est un dentiste il va pas faire des trucs de generaliste"""
    
    def __init__(self):
        Profil.__init__(self)
        self.metier = "metier"

    def saisie(self, prenom, nom, mail, telephone, adresse, metier):
        Profil.saisie(self, prenom, nom, mail, telephone, adresse)
        self.metier = str(metier)

    def __repr__(self):
        return "FICHE DOCTEUR : Medecin " + str(self.metier) + " " + str(self.prenom) + " " + str(self.nom) + "\nDe contact : " + self.mail + " " + str(self.telephone) + "\nau cabinet situé : " + self.adresse


class Patient(Profil):
    """Le patient prends en plus en parametre sa date de naissance, j'ai 
    intentionnellement pas mis le fait qu'il soit majeur en parametre pour
    moi ça me semble pas enormement important alors j'ai défini une fonction
    en dehors mais c'est peut etre plus interessant d'en faire une methode
    et après ça donnera patient.est_majeur() et True/False"""
    
    def __init__(self):
        Profil.__init__(self)
        self.date = [0, 0, 0] #LISTE sous forme [dd, mm, yyyy]
        
    def saisie(self, prenom, nom, mail, telephone, adresse, date):
        Profil.saisie(self, prenom, nom, mail, telephone, adresse)
        self.date = date
    
    def __repr__(self):
        return "FICHE PATIENT : Mr/Mme " + str(self.prenom) + " " + str(self.nom) + "\nné le : " + str(self.date[0]) + " " + MOIS[ self.date[1]-1 ] + " " + str(self.date[2]) + "\nDe contact : " + self.mail + " " + str(self.telephone) + "\nRésidant au : " + self.adresse


def est_majeur(patient, jour):#Prends en entrée une liste [jour, mois, année]
    """Cette fonction retourne True le patient est majeur le jour indiqué et
    False si c'est pas le cas"""
    date_majeur = patient.date
    date_majeur[2] += 18
        
    if jour[2] > date_majeur[2] :
        return True
    elif jour[2] < date_majeur[2] :
        return False
        
    elif jour[1] > date_majeur[1] :
        return True
    elif jour[1] < date_majeur[1] :
        return False
        
    elif jour[0] >= date_majeur[0] :
        return True
    else :
        return False


if __name__ == "__main__" :
    
    doc1 = Docteur()
    doc1.saisie("Vic-Eline", "Carré", "vic.carre@alumni.enac.fr", "0656849331", "87 rue de la vallée de Dana PARIS FRANCE 75 000", "generaliste")
    print(doc1)
    
    patient1 = Patient()
    patient1.saisie("Nathan", "Le-Con", "nathan.ledergerbergerberger@gmail.com", "0655219874", "7 rue de la libération, STRASBOURG, 53 980, FRANCE", [27, 6, 2000])
    print(patient1)

    print (est_majeur(patient1, [26, 6, 2020]))#ça fonctionne
