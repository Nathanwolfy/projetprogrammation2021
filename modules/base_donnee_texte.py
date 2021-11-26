import profil as p

def liste_medecin():
    """cette fonction prends le document texte ou on met nos données en param
    le lit et retourne une liste exploitale de tous les docteurs"""
    liste_praticiens = []
    with open("medecins.txt", "r") as f:
        for line in f:
            l = line.split()
            doc = p.Docteur()
            adresse = ""
            for elt in l[5:]:
                adresse = adresse + " " + elt
            doc.saisie(l[1], l[2], l[3], l[4], adresse, l[0])
            liste_praticiens.append(doc)
    return liste_praticiens


def liste_patient():
    """cette fonction prends le document texte ou on met nos données en param
    le lit et retourne une liste exploitale de tous les patients"""
    liste_patients = []
    with open("patients.txt", "r") as f:
        for line in f:
            l = line.split()
            mec = p.Patient()
            adresse = ""
            date = [ int(l[2]), int(l[3]), int(l[4]) ]
            for elt in l[7:]:
                adresse = adresse + " " + elt
            mec.saisie(l[0], l[1], l[5], l[6], adresse, date)
            liste_patients.append(mec)
    return liste_patients


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
    fichier = open ("patients.txt", "a")
    fichier.writelines("\n" + str(prenom) + " " + str(nom) + " " + str(jour) + " " + str(mois) + " " + str(annee) + " " + str(mail) + " " + str(telephone) + " " + str(adresse))
    fichier.close()
    

if __name__ == "__main__" :
    
    liste_praticiens = liste_medecin()
    #for elt in liste_praticiens:
    #    print (elt)

    liste_malades = liste_patient()
    #for elt in liste_malades:
    #    print (elt)
    
    fin_de_recherche = recherche_patient("frigiel")
    print(fin_de_recherche)
    
    #creer_patient("joseph", "bellobitto", 5, 12, 2001, "jojo.bizarre@venture.com", "0684397515", "Lieu dit Le GENEPI, POILLEY, 76950, FRANCE")
    #ça fonctionne
    creer_patient("edouard", "guehenno", 25, 2, 2019, "ed.pro@gmail.com", "0784943751", "77 avenue Charles de Gaulle, DIJON, 55200, FRANCE")
