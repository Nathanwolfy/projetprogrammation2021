MOIS = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]

class Profil:
    """les parametres communs a tous les profils sont le prenom le nom le mail, 
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
    """le docteur prends en plus en parametre de lui meme son metier 
    ie si c'est un dentiste il va pas faire des trucs de generaliste"""
    
    def __init__(self):
        Profil.__init__(self)
        self.metier = "metier"#STR

    def saisie(self, prenom, nom, mail, telephone, adresse, metier):
        Profil.saisie(self, prenom, nom, mail, telephone, adresse)
        self.metier = str(metier)

    def __repr__(self):
        return "FICHE DOCTEUR : Medecin " + str(self.metier) + " " + str(self.prenom) + " " + str(self.nom) + "\nDe contact : " + self.mail + " " + str(self.telephone) + "\nau cabinet situé : " + self.adresse


class Patient(Profil):
    """le patient prends en plus en parametre sa date de naissance, je n'ai 
    intentionnellement pas mis le fait qu'il soit majeur en parametre pour
    moi ça me semble pas enormement important alors j'ai défini une methode
    en dehors et cela donne patient.est_majeur() = True/False"""
    
    def __init__(self):
        Profil.__init__(self)
        self.date = [0, 0, 0] #LISTE sous forme [dd, mm, yyyy]
        
    def saisie(self, prenom, nom, mail, telephone, adresse, date):
        Profil.saisie(self, prenom, nom, mail, telephone, adresse)
        self.date = date
    
    def __repr__(self):
        return "FICHE PATIENT : Mr/Mme " + str(self.prenom) + " " + str(self.nom) + "\nné le : " + str(self.date[0]) + " " + MOIS[ self.date[1]-1 ] + " " + str(self.date[2]) + "\nDe contact : " + self.mail + " " + str(self.telephone) + "\nRésidant au : " + self.adresse

#piste d'amelioration : faire de cette methode un automatisme avec une fonction
#qui prend en compte le jour ou nous sommes actuellement afin qu'il ne soit pas
#a taper manuellement
    def est_majeur(self, jour):
        """cette methode retourne True : le patient est majeur le jour indique.
        False si ce n'est pas le cas"""
        date_majeur = self.date
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
    
    """
    doc1 = Docteur()
    doc1.saisie("Vic-Eline", "Carré", "vic.carre@alumni.enac.fr", "0656849331", "87 rue de la vallée de Dana PARIS FRANCE 75 000", "generaliste")
    print(doc1)
    """
    
    """
    patient1 = Patient()
    patient1.saisie("nathan", "ledergerbergerberger", "nathan.ledergerbergerberger@gmail.com", "0655219874", "7 rue de la libération, STRASBOURG, 53 980, FRANCE", [27, 6, 2000])
    print(patient1)
    """
    
    """
    print( patient1.est_majeur([26, 7, 2019]) )
    """