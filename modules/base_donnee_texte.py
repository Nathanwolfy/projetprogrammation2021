import profil as p

def liste_medecin():
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

if __name__ == "__main__" :
    
    liste_praticiens = liste_medecin()
    for elt in liste_praticiens:
        print (elt)

    liste_malades = liste_patient()
    for elt in liste_malades:
        print (elt)