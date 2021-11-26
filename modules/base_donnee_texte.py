import profil as p


def lire_bdd_medecin(l):
    """Cette fonction crée le medecin à partir de la liste split() de la base de 
    donnée du document texte."""
    doc = p.Docteur()
    adresse = ""
    for elt in l[5:]:
        adresse = adresse + " " + elt
    doc.saisie(l[1], l[2], l[3], l[4], adresse, l[0])
    return doc
    

def liste_medecin():
    """cette fonction prends le document texte ou on met nos données en param
    le lit et retourne une liste exploitale de tous les docteurs"""
    liste_praticiens = []
    with open("medecins.txt", "r") as f:
        for line in f:
            l = line.split()
            doc = lire_bdd_medecin(l)
            liste_praticiens.append(doc)
    return liste_praticiens


def lire_bdd_patient(l):
    """Cette fonction crée le patient à partir de la liste split() de la base de 
    donnée du document texte."""
    patient = p.Patient()
    adresse = ""
    date = [ int(l[2]), int(l[3]), int(l[4]) ]
    for elt in l[7:]:
        adresse = adresse + " " + elt
    patient.saisie(l[0], l[1], l[5], l[6], adresse, date)
    return patient


def liste_patient():
    """cette fonction prends le document texte ou on met nos données en param
    le lit et retourne une liste exploitale de tous les patients"""
    liste_patients = []
    with open("patients.txt", "r") as f:
        for line in f:
            l = line.split()
            patient = lire_bdd_patient(l)
            liste_patients.append(patient)
    return liste_patients

#On a créé la liste patients et medecins à partir du document texte lesgo

def recherche_patient(string):
    """Cette fonction permet de prendre une chaine de caract en parametre, et retourne parmis tous les 
    patients existants ceux avec une chaine matchante, c'est pour voir si quelqu'un est enregistré et
    avoir accès à ses données"""
    recherche = []
    with open("patients.txt", "r") as f:
        for line in f:
            l = line.split()
            mec = p.Patient()
            adresse = ""
            date = [ int(l[2]), int(l[3]), int(l[4]) ]
            for elt in l[7:]:
                adresse = adresse + " " + elt
                mec.saisie(l[0], l[1], l[5], l[6], adresse, date)
            for i in range(len(l)):
                if l[i] == str(string):
                    recherche.append(mec)
    if recherche == []:
        return "La recherche n'a pas aboutie"
    else:
        return recherche
        
    
def creer_patient(prenom, nom, jour, mois, annee, mail, telephone, adresse):
    """Cette fonction créé un nouveau patient et rentre ses elements dans la base de donée"""
    fichier = open ("patients.txt", "a")
    fichier.writelines(str(prenom) + " " + str(nom) + " " + str(jour) + " " + str(mois) + " " + str(annee) + " " + str(mail) + " " + str(telephone) + " " + str(adresse))
    fichier.close()


def supprimer_patient():
    pass


def modifier_patient(mail):
    """but : modifier la ligne d'un patient à partir de son mail, qui est par définition
    unique"""
    indiceligne = 0
    with open("patients.txt", "r") as f:
        lignes = f.readlines()
        for texte in lignes:
            l = texte.split()
            if l[5] == mail :
                indiceligne = lignes.index(texte)
        #En fait c'est presque plus rapide de supprimer tout et de refaire un
        #fichier avec TOUTES les lignes et voila je pense que c'est bien


if __name__ == "__main__" :
    
    liste_praticiens = liste_medecin()
    #for elt in liste_praticiens:
    #    print (elt)

    liste_malades = liste_patient()
    #for elt in liste_malades:
    #    print (elt)
    #print(liste_malades)
    
    fin_de_recherche = recherche_patient("25")
    #print(fin_de_recherche)
    
    #creer_patient("joseph", "bellobitto", 5, 12, 2001, "jojo.bizarre@venture.com", "0684397515", "Lieu dit Le GENEPI, POILLEY, 76950, FRANCE")
    #ça fonctionne
    #creer_patient("frigiel", "fandefanta", 21, 3, 2009, "fantacoeurfrigiel@yahoo.fr", "07846951", "1 rue samantha Davies, SABLES-OLONNES, 45500, FRANCE")
    
    a = modifier_patient("frigieletfluffy@gmail.de")
    print (a)
