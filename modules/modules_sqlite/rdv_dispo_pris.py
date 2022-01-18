import sqlite3
from . import profil as p
from . import lire_sql as lsql


def suppr_donnees_apres_rdv(jour, mois, annee):
    pass


def journee_existe_pour_ce_medecin(jour, mois, annee, medecin):
    """cette fonction verifie si il existe pour un certain medecin un rendez
    vous dans cette journee au cas ou pour ne pas recreer une journee vide
    dans la bdd par accident"""
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT medecin FROM rdv_dispos WHERE jour = ? AND mois = ? AND annee = ? AND medecin = ?", (jour, mois, annee, medecin))
    rech = cursor.fetchall()
    connection.close()
    if rech == [] :
        return False
    else :
        return True


def temps_motif(type_de_medecin, motif):
    """cette fonction retourne le temps que dure un tel motif de rendez vous
    pour un tel medecin"""
    #print(lsql.liste_type_medecin())
    #print(lsql.liste_type_de_medecin_et_rdv_pris())
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT temps FROM rdvs WHERE type_de_medecin = ? AND motif = ?", (type_de_medecin, motif))
    rech = cursor.fetchone()
    connection.close()
    return rech[0]


def rdv_dispo(jour, mois, annee, heure, minute, medecin):
    """cette fonction renvoie true si le rendez vous est disponible et renvoie
    false si le rendez vous n'est pas disponible"""
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT dispo FROM rdv_dispos WHERE jour = ? AND mois = ? AND annee = ? AND heure = ? AND minute = ? AND medecin = ?", (jour, mois, annee, heure, minute, medecin))
    rech = cursor.fetchone()
    connection.close()
    if rech == None or rech[0] == 0 :
        return False
    else :
        return True


#a faire : -> creer une securite : si le rdv est pris 
#renvoyer que ce n'est pas possible
def passer_creneau_dispo_en_creneau_pris(jour, mois, annee, heure, minute, medecin):
    """cette fonction fait passer une tranche de 15 minutes d'un medecin en
    non disponible en passant la disponibilite a 0"""    
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    #ne sachant pas comment utiliser un WHERE et un VALUES dans la meme
    #requete, il va falloir supprimer et recreer un rdv ce qui n'est pas le 
    #¼plus optimise a mon avis mais des que j'ai le temps je demande au prof
    cursor.execute("DELETE FROM rdv_dispos WHERE jour = ? AND mois = ? AND annee = ? AND heure = ? AND minute = ? AND medecin = ?", (jour, mois, annee, heure, minute, medecin))
    connection.commit()
    cursor.execute("INSERT INTO rdv_dispos VALUES (?,?,?,?,?,?,?)", (jour, mois, annee, heure, minute, medecin, 0))
    connection.commit()
    connection.close()


def creneau_possible_max(jour, mois, annee, heure, minute, medecin):
    """cette fonction renvoie le nombre de creneaux max de 15 minutes que le
    patient a devant lui pour prendre le rendez vous"""
    nbr_max = 0
    #if rdv_dispo(jour, mois, annee, heure, minute, medecin):
    #    nbr_max = 1
    
    while heure != 12 and heure != 19 and rdv_dispo(jour, mois, annee, heure, minute, medecin) :
        if minute == 45 :
            minute = 0
            heure += 1
        else :
            minute += 15
        nbr_max += 1

    return nbr_max
    


def passer_rdv_dispo_en_rdv_pris(jour, mois, annee, heure, minute, medecin, temps):
    """cette fonction permet de bloquer plusieurs creneaux de 15 minutes
    pour des rendez vous qui dure plus longtemps"""
    nbr_de_creneaux = temps//15
    creneaux_max = creneau_possible_max(jour, mois, annee, heure, minute, medecin)
    if nbr_de_creneaux <= creneaux_max:
        for i in range(nbr_de_creneaux):
            passer_creneau_dispo_en_creneau_pris(jour, mois, annee, heure, minute, medecin)
            if minute == 45 :
                minute = 0
                heure += 1
            else :
                minute += 15
    else:
        #return "probleme de temps"
        pass
    



#amelioration dans le futur : creer une facon de faire une demi journee voir 
#gerer l'amplitude horaire journaliere d'un medecin et sa pause dejeuner
def creer_journee_vide(jour, mois, annee, medecin):
    """cette fonction cree une journee vide remplie de rdv disponibles pour un
    certain medecin, avec debut 8h00 et fin 19h00 et une heure pour manger 
    entre midi et 13h"""
    if journee_existe_pour_ce_medecin(jour, mois, annee, medecin) == False:
        connection = lsql.connection_bdd()
        cursor = connection.cursor()
        for i in range(8, 19):
            donnee_a_implementer = (jour, mois, annee, i, 0, medecin, 1)
            cursor.execute("INSERT INTO rdv_dispos VALUES (?,?,?,?,?,?,?)", donnee_a_implementer)
            connection.commit()
        for i in range(8, 19):
            donnee_a_implementer = (jour, mois, annee, i, 15, medecin, 1)
            cursor.execute("INSERT INTO rdv_dispos VALUES (?,?,?,?,?,?,?)", donnee_a_implementer)
            connection.commit()
        for i in range(8, 19):
            donnee_a_implementer = (jour, mois, annee, i, 30, medecin, 1)
            cursor.execute("INSERT INTO rdv_dispos VALUES (?,?,?,?,?,?,?)", donnee_a_implementer)
            connection.commit()
        for i in range(8, 19):
            donnee_a_implementer = (jour, mois, annee, i, 45, medecin, 1)
            cursor.execute("INSERT INTO rdv_dispos VALUES (?,?,?,?,?,?,?)", donnee_a_implementer)
            connection.commit()
        cursor.execute('DELETE FROM rdv_dispos WHERE heure=?' ,(12,))
        connection.commit()
        connection.close()
    else :
        #return("ce medecin a deja la journee de creee")
        pass


def rdv_disponible(jour, mois, annee, medecin, temps):
    """renvoie une liste pour louis des rendez vous disponibles selon le temps
    qu'il souhaite et le medecin qu'il souhaite"""
    creneau = temps//15
    liste_creneaux_possibles = []
    for i in range(8,12):
        if creneau <= creneau_possible_max(jour, mois, annee, i, 0, medecin):
            liste_creneaux_possibles.append(f"{i}:00")
        if creneau <= creneau_possible_max(jour, mois, annee, i, 15, medecin):
            liste_creneaux_possibles.append(f"{i}:15")
        if creneau <= creneau_possible_max(jour, mois, annee, i, 30, medecin):
            liste_creneaux_possibles.append(f"{i}:30")
        if creneau <= creneau_possible_max(jour, mois, annee, i, 45, medecin):
            liste_creneaux_possibles.append(f"{i}:45")
    for i in range(13,19):
        if creneau <= creneau_possible_max(jour, mois, annee, i, 0, medecin):
            liste_creneaux_possibles.append(f"{i}:00")
        if creneau <= creneau_possible_max(jour, mois, annee, i, 15, medecin):
            liste_creneaux_possibles.append(f"{i}:15")
        if creneau <= creneau_possible_max(jour, mois, annee, i, 30, medecin):
            liste_creneaux_possibles.append(f"{i}:30")
        if creneau <= creneau_possible_max(jour, mois, annee, i, 45, medecin):
            liste_creneaux_possibles.append(f"{i}:45")
    return liste_creneaux_possibles

def date(jour, mois, annee):
    """cette fonction est utile pour l'affichage, elle transforme trois
    chiffres ( par exemple 17 03 2020 ) en une string affichable par Qt
    ( ici : lundi 17 mars 2020 )"""
    connection = lsql.connection_bdd_calendrier()
    cursor = connection.cursor()
    cursor.execute("SELECT nom_jour FROM calendrier WHERE nb_jour = ? AND mois_jour = ? AND annee = ?", (jour, mois, annee))
    nom_du_jour = cursor.fetchone()
    connection.close()
    return f"{nom_du_jour[0]} {jour} {p.MOIS[mois-1]} {annee}"
    
def affichage_final_rdv_dispo(jour, mois, annee, medecin, temps):
    """cette fonction renvoie les rendez vous disponibles par date donnee pour
    medecin donne et pour delai donne dans une journee entiere comme le fait 
    doctolib"""
    return [date(jour, mois, annee), rdv_disponible(jour, mois, annee, medecin, temps)]


def medecins_disponibilites_avec_localisation(type_de_medecin, type_de_rdv, ville, jour, mois, annee):
    """cette fonction prends en etree un type de medecin, un motif de rendez 
    vous, une ville, une date afin de ressortir dans une ville precise, les 
    emplois du temps des medecins precisement qui peuvent accomplir cette 
    consultation"""
    medecins_de_ce_type_et_de_cette_ville = []
    medecins_de_ce_type_et_de_cette_ville_id = []
    liste_des_rdv_disponibles = []
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT prenom, nom, ville, mail FROM medecins WHERE travail = ?", (type_de_medecin,))
    medecins_de_ce_type = cursor.fetchall()
    for elt in medecins_de_ce_type:
        if elt[2] == ville.upper() :
            medecins_de_ce_type_et_de_cette_ville.append("Dr " + elt[0] + " " + elt[1])
            medecins_de_ce_type_et_de_cette_ville_id.append(elt[3])
    connection.close()
    
    temps = temps_motif(type_de_medecin, type_de_rdv)
    for elt in medecins_de_ce_type_et_de_cette_ville_id:
        liste_des_rdv_disponibles.append(rdv_disponible(jour, mois, annee, elt, temps))
    
    dictionnaire_medecins_et_leur_disponibilites = {}
    for i in range(len(medecins_de_ce_type_et_de_cette_ville)):
        dictionnaire_medecins_et_leur_disponibilites[medecins_de_ce_type_et_de_cette_ville[i]] = liste_des_rdv_disponibles[i]
    return dictionnaire_medecins_et_leur_disponibilites

def profil_medecin_complet(string):
    """cette fonction prends une string du type "Dr Prenom Nom" et les
    donnees personnelles du medecin sont renvoyes"""
    liste_attribut = string.split()
    prenom = liste_attribut[1]
    nom = liste_attribut[2]
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT mail,telephone,rue,code_postal,ville FROM medecins WHERE prenom = ? AND nom = ?", (prenom, nom))
    donnees_personnelles_du_medecin_demande = cursor.fetchone()
    connection.close()
    return donnees_personnelles_du_medecin_demande