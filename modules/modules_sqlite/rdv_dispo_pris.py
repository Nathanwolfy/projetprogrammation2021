import sqlite3
import lire_sql as lsql
#faire une fonction qui prends un jour donne et supprime TOUT de ce jour et 
#des jours d'avants


def suppr_donnees_apres_rdv(jour, mois, annee):
    pass


def journee_existe_pour_ce_medecin(jour, mois, annee, medecin):
    """cette fonction verifie si il existe pour un certain medecin un rendez
    vous dans cette journee au cas ou pour ne pas recreer une journee vide
    dans la bdd par accident"""
    connection = sqlite3.connect("donnees.db")
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
    print(lsql.liste_type_medecin())
    print(lsql.liste_type_de_medecin_et_rdv_pris())
    connection = sqlite3.connect("donnees.db")
    cursor = connection.cursor()
    cursor.execute("SELECT temps FROM rdvs WHERE type_de_medecin = ? AND motif = ?", (type_de_medecin, motif))
    rech = cursor.fetchone()
    connection.close()
    return rech[0]


def rdv_dispo(jour, mois, annee, heure, minute, medecin):
    """cette fonction renvoie true si le rendez vous est disponible et renvoie
    false si le rendez vous n'est pas disponible"""
    connection = sqlite3.connect("donnees.db")
    cursor = connection.cursor()
    cursor.execute("SELECT dispo FROM rdv_dispos WHERE jour = ? AND mois = ? AND annee = ? AND heure = ? AND minute = ? AND medecin = ?", (jour, mois, annee, heure, minute, medecin))
    rech = cursor.fetchone()
    connection.close()
    if rech[0] == 0 :
        return False
    else :
        return True


#creer une securite si le rdv est pris renvoyer que ce n'est pas possible
#pour les motifs et patients des rendez vous faire une deuxieme bdd je pense
def passer_creneau_dispo_en_creneau_pris(jour, mois, annee, heure, minute, medecin):
    """cette fonction fait passer une tranche de 15 minutes d'un medecin en
    non disponible en passant la disponibilite a 0"""    
    connection = sqlite3.connect("donnees.db")
    cursor = connection.cursor()
    #ne sachant pas comment utiliser un WHERE et un VALUES dans la meme
    #requete, il va falloir supprimer et recreer un rdv
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
        return "probleme de temps"
    



#amelioration dans le futur : creer une facon de faire une demi journee voir 
#gerer l'amplitude horaire journaliere d'un medecin et sa pause dej
def creer_journee_vide(jour, mois, annee, medecin):
    """cette fonction cree une journee vide remplie de rdv disponibles pour un
    certain medecin, avec debut 8h00 et fin 19h00 et une heure pour manger 
    entre midi et 13h"""
    if journee_existe_pour_ce_medecin(jour, mois, annee, medecin) == False:
        connection = sqlite3.connect("donnees.db")
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
        print("ce medecin a deja la journee de creee")


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
    connection = sqlite3.connect("calendrier.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO rdv_dispos VALUES (?,?,?,?,?,?,?)", donnee_a_implementer)
    connection.commit()
    connection.close()
    date_str = 
    


if __name__ == "__main__" :
    
    """
    creer_journee_vide(27, 1, 2022, "jules.muscle.bg@bing.fr")
    """
    
    """
    journee_existe_pour_ce_medecin(27, 1, 2022, "sipha@lecheque.com")
    """
    
    """
    passer_creneau_dispo_en_creneau_pris(27, 1, 2022, 8, 30, "sipha@lecheque.com")
    """
    
    """
    rdv_dispo(27, 1, 2022, 8, 30, "sipha@lecheque.com")
    """
    
    """
    temps_motif()
    """
    
    """
    temps_motif("generaliste", "certificat medical")
    """
    
    """
    passer_rdv_dispo_en_rdv_pris(27, 1, 2022, 13, 30, "sipha@lecheque.com", 60)
    """
    
    """
    creneau_possible_max(27, 1, 2022, 11, 15, "sipha@lecheque.com")
    """
    
    """
    rdv_disponible(27, 1, 2022, "sipha@lecheque.com", 60)
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    