MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"]

class Profil:
    
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
    
    def __init__(self):
        Profil.__init__(self)

    def __repr__(self):
        return "FICHE DOCTEUR : Docteur " + str(self.prenom) + " " + str(self.nom) + "\nDe contact : " + self.mail + " " + str(self.telephone) + "\nau cabinet situé : " + self.adresse

class Patient(Profil):
    
    def __init__(self):
        Profil.__init__(self)
        self.date = [0, 0, 0] #LISTE sous forme [dd, mm, yyyy]
        
    def saisie(self, prenom, nom, mail, telephone, adresse, date):
        Profil.saisie(self, prenom, nom, mail, telephone, adresse)
        self.date = date
    
    #def est_majeur(jour):
     #   if blablabla:
    
    def __repr__(self):
        return "FICHE PATIENT : Mr/Mme " + str(self.prenom) + " " + str(self.nom) + "\nné le : " + str(self.date[0]) + " " + MOIS[ self.date[1]-1 ] + " " + str(self.date[2]) + "\nDe contact : " + self.mail + " " + str(self.telephone) + "\nRésidant au : " + self.adresse




if __name__ == "__main__" :
    
    doc1 = Docteur()
    doc1.saisie("Vic-Eline", "Carré", "vic.carre@alumni.enac.fr", "0656849331", "87 rue de la vallée de Dana PARIS FRANCE 75 000")
    print(doc1)
    
    patient1 = Patient()
    patient1.saisie("Nathan", "Le-Con", "nathan.ledergerbergerberger@gmail.com", "0655219874", "7 rue de la libération, STRASBOURG, 53 980, FRANCE", [27, 6, 2000])
    print(patient1)


