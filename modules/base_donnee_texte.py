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


if __name__ == "__main__" :
    
"""
    liste_paticiens = liste_medecin()
    print(liste_paticiens)
"""

"""
    liste_malades = liste_patient()
    print(liste_malades)
"""
