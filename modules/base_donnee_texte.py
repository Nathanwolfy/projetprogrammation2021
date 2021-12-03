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

def supprimer_patient(mail):
    """ce programme permet de supprimer un patient de la base de donnée en supprimant ses 
    données également"""
    indligne = indice_ligne_patient(mail)
    if indligne == -1:
        return "le patient que vous essayez de supprimer n'existe pas encore sur doctobélix"
    else :
        with open("patients.txt", "r") as f:
            lignes = f.readlines()
        lignes.pop(indligne - 1)
        with open("patients.txt", "w") as f:
            f.writelines(lignes.strip("\n"))

"""
def supprimer_patient(mail):
    indligne = indice_ligne_patient(mail)
    if indligne == -1:
        return "le patient que vous essayez de supprimer n'existe pas encore sur doctobélix"
    else :
        with open("patients.txt", "r") as f:
            lignes = f.readlines()
        deleted_text = lignes.pop(indligne - 1)
        with open("patients.txt", "w") as f:
            for ligne in lignes:
                if ligne != str(deleted_text) + "\n" :
                    f.write(ligne)
"""

def modifier_patient(prenom, nom, jour, mois, annee, mail, telephone, adresse):
    """but : modifier la ligne d'un patient à partir de son mail, qui est par définition
    unique"""
    indligne = indice_ligne_patient(mail)
    if indligne == -1:
        return "Le patient à modifier n'a pas été trouvé dans notre application doctobélix"
    else:
        supprimer_patient(mail)
        creer_patient(prenom, nom, jour, mois, annee, mail, telephone, adresse)
    #return indiceligne
        #En fait c'est presque plus rapide de supprimer tout et de refaire un
        #fichier avec TOUTES les lignes et voila je pense que c'est bien
        #aussi ajouter dans la fonction recherche l'utilisation de lire_bdd_patient(l)
#On a créé la liste patients et medecins à partir du document texte lesgo



if __name__ == "__main__" :
    

    liste_paticien = liste_medecin()
    #for elt in liste_praticiens:
    #    print (elt)

    liste_malades = liste_patient()
    #for elt in liste_malades:
    #    print (elt)
    #print(liste_malades)
    
    fin_de_recherche = recherche_patient("25")
    #print(fin_de_recherche)
    
    a = indice_ligne_patient("ed.pro@gmail.com")
    #print(a)
    b = indice_ligne_patient("jojo.bizarre@venture.com")
    #print(b)
    c = indice_ligne_patient("the.weng.06@gmail.com")
    #print(c)
    
    #creer_patient("joseph", "bellobitto", 5, 12, 2001, "jojo.bizarre@venture.com", "0684397515", "Lieu dit Le GENEPI, POILLEY, 76950, FRANCE")
    #ça fonctionne
    d = creer_patient("frigiel", "fandefanta", 21, 3, 2009, "fantacoeurfrigiel@yahoo.fr", "07846951", "1 rue samantha Davies, SABLES-OLONNES, 45500, FRANCE")
    #print(d)
    
    e = supprimer_patient("fantacoeurfrigiel@yahoo.fr")  
    #print(e)
    
    #d = modifier_patient("ed.pro@gmail.com")
    #print (d)

    liste_paticiens = liste_medecin()
    print (liste_paticiens)

    liste_malades = liste_patient()
    print (liste_malades)
