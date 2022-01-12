import sqlite3
import time

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Wen", "Sat", "Sun"]
MOIS = [i for i in range(1, 13)] #[1 #Janvier, 2 #Février, ...]

def nb_jours_dans_un_mois(mois, annee): 
    if mois == 2: #Février
        if annee % 4 == 0:
            return 29 #année bissextile
        else:
            return 28 #année non bissextile
    elif mois < 8 and mois%2 == 1:
        return 31
    elif mois >=8 and mois%2 == 0:
        return 31
    return 30

now = time.localtime(time.time())
actual_time = time.strftime("%a %d %m %Y", now) #nom_jour (english) nb_jour mois annee
nom_jour = JOURS[DAYS.index(actual_time[:3])]
date_actuelle = nom_jour + ' ' + actual_time[4:]
D = date_actuelle.split()
nb_jour = int(D[1])
mois_jour = int(D[2])
annee = int(D[3])
nb_jour_suivant = nb_jour + 1
mois_jour_suivant = mois_jour
if JOURS.index(nom_jour) == len(JOURS) - 1:
    nom_jour_suivant = "Lundi"
else:
    nom_jour_suivant = JOURS[JOURS.index(nom_jour)+1]

while nb_jour_suivant != nb_jour and mois_jour_suivant != mois_jour: #[Lundi 3 Janvier, Mardi 4 Janvier, Mercredi 5 Janvier, ...]
    if JOURS.index(nom_jour) == len(JOURS) - 1:
        nom_jour_suivant = "Lundi"
    else:
        indice = JOURS.index(nom_jour)
        nom_jour_suivant = JOURS[indice + 1]
    if nb_jour_suivant < nb_jours_dans_un_mois(mois_jour_suivant, annee):
        nb_jour_suivant += 1
    else:
        if mois_jour_suivant == 12:
            mois_jour_suivant = 1
            annee += 1
        else:
            mois_jour_suivant += 1
        nb_jour_suivant = 1
if nb_jour < 10:
    str_nb_jour = '0' + str(nb_jour)
else:
    str_nb_jour = str(nb_jour)
if mois_jour < 10:
    str_mois_jour = '0' + str(mois_jour)
else:
    str_mois_jour = str(mois_jour)
date_dans_un_an = nom_jour_suivant + ' ' + str_nb_jour + ' ' + str_mois_jour + ' ' + str(annee + 1)

def connection():
    try:
        connect = sqlite3.connect('calendrier.db')
        return connect
    except Exception as e:
        print(e)
        print('La connexion n\'a pas pu être établie.')


con = connection()
cursor = con.cursor()

cursor.execute('SELECT id_jour FROM calendrier')
rows = cursor.fetchall()
id_1 = int(rows[0][0])
id_2 = int(rows[-1][0])

#supprime les jours avant la date d'aujourd'hui
cursor.execute('SELECT nom_jour FROM calendrier WHERE id_jour=?', (id_1,))
nom_premier_jour = cursor.fetchone()[0]
cursor.execute('SELECT nb_jour FROM calendrier WHERE id_jour=?', (id_1,))
nb_premier_jour = cursor.fetchone()[0]
cursor.execute('SELECT mois_jour FROM calendrier WHERE id_jour=?', (id_1,))
mois_premier_jour = cursor.fetchone()[0]
cursor.execute('SELECT annee FROM calendrier WHERE id_jour=?', (id_1,))
annee_premier_jour = cursor.fetchone()[0]
if nb_premier_jour < 10:
    str_nb_premier_jour = '0' + str(nb_premier_jour)
else:
    str_nb_premier_jour = str(nb_premier_jour)
if mois_premier_jour < 10:
    str_mois_premier_jour = '0' + str(mois_premier_jour)
else:
    str_mois_premier_jour = str(mois_premier_jour)
premier_jour = nom_premier_jour + ' ' + str_nb_premier_jour + ' ' + str_mois_premier_jour + ' ' + str(annee_premier_jour)

id_1 = id_1 - 1
list_id = []
while premier_jour != date_actuelle:
    if JOURS.index(nom_premier_jour) == len(JOURS) - 1:
        nom_premier_jour = "Lundi"
    else:
        indice = JOURS.index(nom_premier_jour)
        nom_premier_jour = JOURS[indice + 1]
    if nb_premier_jour < nb_jours_dans_un_mois(mois_premier_jour, annee_premier_jour):
        nb_premier_jour += 1
        id_1 += 1
        list_id.append((id_1,))
        if nb_premier_jour < 10:
            str_nb_premier_jour = '0' + str(nb_premier_jour)
        else:
            str_nb_premier_jour = str(nb_premier_jour)
        if mois_premier_jour < 10:
            str_mois_premier_jour = '0' + str(mois_premier_jour)
        else:
            str_mois_premier_jour = str(mois_premier_jour)
        premier_jour = nom_premier_jour + ' ' + str_nb_premier_jour + ' ' + str_mois_premier_jour + ' ' + str(annee_premier_jour)
    else:
        if mois_premier_jour == 12:
            mois_premier_jour = 1
            annee_premier_jour += 1
        else:
            mois_premier_jour += 1
        nb_premier_jour = 1
        id_1 += 1
        list_id.append((id_1,))
        if nb_premier_jour < 10:
            str_nb_premier_jour = '0' + str(nb_premier_jour)
        else:
            str_nb_premier_jour = str(nb_premier_jour)
        if mois_premier_jour < 10:
            str_mois_premier_jour = '0' + str(mois_premier_jour)
        else:
            str_mois_premier_jour = str(mois_premier_jour)
        premier_jour = nom_premier_jour + ' ' + str_nb_premier_jour + ' ' + str_mois_premier_jour + ' ' + str(annee_premier_jour)

cursor.executemany('DELETE FROM calendrier WHERE id_jour=?', list_id)
con.commit()

cursor.execute('SELECT nom_jour FROM calendrier WHERE id_jour=?', (id_2,))
nom_dernier_jour = cursor.fetchone()[0]
cursor.execute('SELECT nb_jour FROM calendrier WHERE id_jour=?', (id_2,))
nb_dernier_jour = cursor.fetchone()[0]
cursor.execute('SELECT mois_jour FROM calendrier WHERE id_jour=?', (id_2,))
mois_dernier_jour = cursor.fetchone()[0]
cursor.execute('SELECT annee FROM calendrier WHERE id_jour=?', (id_2,))
annee_dernier_jour = cursor.fetchone()[0]
if nb_dernier_jour < 10:
    str_nb_dernier_jour = '0' + str(nb_dernier_jour)
else:
    str_nb_dernier_jour = str(nb_dernier_jour)
if mois_dernier_jour < 10:
    str_mois_dernier_jour = '0' + str(mois_dernier_jour)
else:
    str_mois_dernier_jour = str(mois_dernier_jour)
dernier_jour = nom_dernier_jour + ' ' + str_nb_dernier_jour + ' ' + str_mois_dernier_jour + ' ' + str(annee_dernier_jour)


#complète le calendrier pour qu'on puisse potentiellement prendre un rdv un an à l'avance 

list_jour = []
while dernier_jour != date_dans_un_an:
    if JOURS.index(nom_dernier_jour) == len(JOURS) - 1:
        nom_dernier_jour = "Lundi"
    else:
        indice = JOURS.index(nom_dernier_jour)
        nom_dernier_jour = JOURS[indice + 1]
    if nb_dernier_jour < nb_jours_dans_un_mois(mois_dernier_jour, annee_dernier_jour):
        nb_dernier_jour += 1
        id_2 += 1
        list_jour.append((id_2, nom_dernier_jour, nb_dernier_jour, mois_dernier_jour, annee_dernier_jour))
        if nb_dernier_jour < 10:
            str_nb_dernier_jour = '0' + str(nb_dernier_jour)
        else:
            str_nb_dernier_jour = str(nb_dernier_jour)
        if mois_dernier_jour < 10:
            str_mois_dernier_jour = '0' + str(mois_dernier_jour)
        else:
            str_mois_dernier_jour = str(mois_dernier_jour)
        dernier_jour = nom_dernier_jour + ' ' + str_nb_dernier_jour + ' ' + str_mois_dernier_jour + ' ' + str(annee_dernier_jour)
    else:
        if mois_dernier_jour == 12:
            mois_dernier_jour = 1
            annee_dernier_jour += 1
        else:
            mois_dernier_jour += 1
        nb_dernier_jour = 1
        id_2 += 1
        list_jour.append((id_2, nom_dernier_jour, nb_dernier_jour, mois_dernier_jour, annee_dernier_jour))
        if nb_dernier_jour < 10:
            str_nb_dernier_jour = '0' + str(nb_dernier_jour)
        else:
            str_nb_dernier_jour = str(nb_dernier_jour)
        if mois_dernier_jour < 10:
            str_mois_dernier_jour = '0' + str(mois_dernier_jour)
        else:
            str_mois_dernier_jour = str(mois_dernier_jour)
        dernier_jour = nom_dernier_jour + ' ' + str_nb_dernier_jour + ' ' + str_mois_dernier_jour + ' ' + str(annee_dernier_jour)




cursor.executemany("INSERT INTO calendrier VALUES (?, ?, ?, ?, ?)", list_jour)
con.commit()

con.close()
