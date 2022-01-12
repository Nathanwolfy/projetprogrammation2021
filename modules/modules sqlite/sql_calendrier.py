import sqlite3

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
MOIS = [i for i in range(1, 13)] #[1 #Janvier, 2 #Février, ...]


def nb_jours_dans_un_mois(mois, annee): 
    if mois == 2: #Février
        if annee % 4 == 0:
            return 29 #année bissextile
        else:
            return 28 #année non bissextile
    elif mois%2 == 0:
        return 31
    elif mois == 7:
        return 31
    return 30


def connection():
    try:
        connect = sqlite3.connect('calendrier.db')
        return connect
    except Exception as e:
        print(e)
        print('La connexion n\'a pas pu être établie.')


con = connection()
cursor = con.cursor()
list_jour = []
#boucle pour faire le calendrier
nom_jour = "Lundi"
nb_jour = 3
mois_jour = 1
annee = 2022
list_jour.append((cursor.lastrowid, nom_jour, nb_jour, mois_jour, annee))
for i in range(365): #[Lundi 3 Janvier, Mardi 4 Janvier, Mercredi 5 Janvier, ...]
    if JOURS.index(nom_jour) == len(JOURS) - 1:
        nom_jour = "Lundi"
    else:
        indice = JOURS.index(nom_jour)
        nom_jour = JOURS[indice + 1]
    if nb_jour < nb_jours_dans_un_mois(mois_jour, annee):
        nb_jour += 1
        list_jour.append((cursor.lastrowid, nom_jour, nb_jour, mois_jour, annee))
    else:
        if mois_jour == 12:
            mois_jour = 1
            annee += 1
        else:
            mois_jour += 1
        nb_jour = 1
        list_jour.append((cursor.lastrowid, nom_jour, nb_jour, mois_jour, annee))
    


cursor.executemany("INSERT INTO calendrier VALUES (?, ?, ?, ?, ?)", list_jour)
con.commit()
con.close()
    
