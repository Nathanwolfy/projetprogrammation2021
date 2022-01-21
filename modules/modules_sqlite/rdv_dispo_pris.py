import sqlite3
from . import profil as p
from . import lire_sql as lsql


def journee_existe_pour_ce_medecin(jour, mois, annee, medecin):
    """cette fonction verifie si il existe pour un certain medecin un rendez
    vous dans cette journee au cas ou pour ne pas recreer une journee vide
    dans la bdd par accident, elle renvoie alors un booleen : True = ce 
    medecin a deja des choses de prevu ce jour (des rendez vous vides ou non)
    et False = rien n'est prevu ce jour"""
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT medecin FROM rdv_dispos WHERE jour = ? AND mois = ? AND annee = ? AND medecin = ?", (jour, mois, annee, medecin))
    rech = cursor.fetchall()
    connection.close()
    if rech == None or rech == [] :
        return False
    else :
        return True


def temps_motif(type_de_medecin, motif):
    """cette fonction retourne le temps que dure un tel motif de rendez vous
    pour un tel type de medecin, elle est tres utile par la suite pour 
    faire le lien entre plusieurs fonctions qui s'adresses plus a un usage
    interne ou bien a un usage client"""
    #print(lsql.liste_type_medecin())
    #print(lsql.liste_type_de_medecin_et_rdv_pris())
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT temps FROM rdvs WHERE type_de_medecin = ? AND motif = ?", (type_de_medecin, motif))
    rech = cursor.fetchone()#fetchone car c'est unique ici, nous n'avons pas besoin d'un fetchmany ou d'un fetchall
    connection.close()
    if rech == None :
        pass
    else :
        return rech[0]


def rdv_dispo(jour, mois, annee, heure, minute, medecin):
    """cette fonction renvoie true si le rendez vous est disponible et renvoie
    false si le rendez vous n'est pas disponible, pour medecin donne (mail)
    jour mois annee heure et minute"""
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
    non disponible en passant la disponibilite a 0, pour ne pas m'y perdre : 
    sont referees ici sous forme de creneaux les tranches indivisibles de 15 
    minutes, les rendez vous sont definis comme des sommes de creneaux."""    
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    #ne sachant pas comment utiliser un WHERE et un VALUES dans la meme
    #requete, il va falloir supprimer et recreer un rdv ce qui n'est pas le 
    #plus optimise a mon avis ceci est une possible amelioration de doctolibre
    cursor.execute("DELETE FROM rdv_dispos WHERE jour = ? AND mois = ? AND annee = ? AND heure = ? AND minute = ? AND medecin = ?", (jour, mois, annee, heure, minute, medecin))
    connection.commit()
    cursor.execute("INSERT INTO rdv_dispos VALUES (?,?,?,?,?,?,?)", (jour, mois, annee, heure, minute, medecin, 0))
    connection.commit()
    connection.close()


def creneau_possible_max(jour, mois, annee, heure, minute, medecin):
    """cette fonction renvoie le nombre de creneaux maximum a la suite 
    de disponibilite pour le medecin a un jour donne, pour une heure et 
    minute donnee, cette fonction permettra de savoir par exemple si 
    un rendez vous d'une certaine longueur peut y etre case ou non"""
    nbr_max = 0
    #if rdv_dispo(jour, mois, annee, heure, minute, medecin):
    #    nbr_max = 1
    
    while heure != 12 and heure != 19 and rdv_dispo(jour, mois, annee, heure, minute, medecin) :
        if minute == 45 :
            minute = 0
            heure += 1#la fonction s'arrete si l'heure depasse la fin de journee qui est 19h ou que le rendez vous empiete sur la pause du midi
        else :#Si ce n'est pas le cas alors la fonction regarde pour le creneau suivant la disponibilite
            minute += 15
        nbr_max += 1

    return nbr_max
    


def passer_rdv_dispo_en_rdv_pris(jour, mois, annee, heure, minute, medecin, temps):
    """cette fonction permet de bloquer plusieurs creneaux de 15 minutes
    pour des rendez vous qui sont des sommes de creneaux, avec en securite 
    la verification que le rendez vou rentre bien dans l'emploi du temps
    du medecin avec la fonction juste au dessus creneau_possible_max"""
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
    entre midi et 13h, pour ne pas avoir trop de parametres j'ai choisi de 
    fixer les horaires des medecins"""
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
    """cette fonction renvoie une liste pour louis des rendez vous disponibles
     selon le temps qu'il souhaite que le rendez vous dure et le medecin qu'il
     souhaite un jour precis donne"""
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
    ( ici : lundi 17 mars 2020 ) grace a la base de donnee calendrier 
    remplie par les fonctions de Vic"""
    connection = lsql.connection_bdd_calendrier()
    cursor = connection.cursor()
    cursor.execute("SELECT nom_jour FROM calendrier WHERE nb_jour = ? AND mois_jour = ? AND annee = ?", (jour, mois, annee))
    nom_du_jour = cursor.fetchone()
    connection.close()
    return f"{nom_du_jour[0]} {jour} {p.MOIS[mois-1]} {annee}"
    
def affichage_final_rdv_dispo(jour, mois, annee, medecin, temps):
    """cette fonction renvoie les rendez vous disponibles pour date donnee pour
    medecin donne et pour delai donne dans une journee entiere comme le fait 
    doctolib, pour Louis"""
    return [date(jour, mois, annee), rdv_disponible(jour, mois, annee, medecin, temps)]


def medecins_disponibilites_avec_localisation(type_de_medecin, type_de_rdv, ville, jour, mois, annee):
    """cette fonction prends en entree un type de medecin, un motif de rendez 
    vous, une ville, une date afin de ressortir dans une ville precise, les 
    emplois du temps des medecins precisement qui peuvent accomplir cette 
    consultation"""
    medecins_de_ce_type_et_de_cette_ville = []#stocke les informations de prenom nom
    medecins_de_ce_type_et_de_cette_ville_id = []#stocke dans les memes indices les informations de mail (cle primaire de la base)
    liste_des_rdv_disponibles = []
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT prenom, nom, ville, mail FROM medecins WHERE travail = ?", (type_de_medecin,))
    medecins_de_ce_type = cursor.fetchall()
    for elt in medecins_de_ce_type:
        if elt[2] == ville.upper() :#ville.upper() pour comparer efficement tous type d'ecriture
            medecins_de_ce_type_et_de_cette_ville.append("Dr " + elt[0] + " " + elt[1])#pour l'affichage
            medecins_de_ce_type_et_de_cette_ville_id.append(elt[3])#les mails ici
    connection.close()
    
    temps = temps_motif(type_de_medecin, type_de_rdv)
    for elt in medecins_de_ce_type_et_de_cette_ville_id:
        liste_des_rdv_disponibles.append(rdv_disponible(jour, mois, annee, elt, temps))#pour l'affichage il nous faut egalement une liste des rdv disponible par medecin (meme indice) et par jour precis
    
    dictionnaire_medecins_et_leur_disponibilites = {}#de fait comme seul des strings passent de client a serveur et que j'ai fait une fonction string to dict parce que Louis ne peu recevoir des dictionnaire, un dictionnaire d'information est la forme privilegiee pour ce genre de contenu
    for i in range(len(medecins_de_ce_type_et_de_cette_ville)):
        dictionnaire_medecins_et_leur_disponibilites[medecins_de_ce_type_et_de_cette_ville[i]] = liste_des_rdv_disponibles[i]
    return dictionnaire_medecins_et_leur_disponibilites#ce dictionnaire renvoie : medecin precis d'un cote et leur disponibilites en ce jour

def profil_medecin_complet(string):
    """cette fonction prends une string du type "Dr Prenom Nom" et les
    donnees personnelles du medecin sont renvoyees, c'est pour l'affichage
    du bilan du rendez vous a la fin de doctolibre cote patient"""
    liste_attribut = string.split()
    prenom = liste_attribut[1]
    nom = liste_attribut[2]
    connection = lsql.connection_bdd()
    cursor = connection.cursor()
    cursor.execute("SELECT mail,telephone,rue,code_postal,ville FROM medecins WHERE prenom = ? AND nom = ?", (prenom, nom))
    donnees_personnelles_du_medecin_demande = cursor.fetchone()
    connection.close()
    return donnees_personnelles_du_medecin_demande

if __name__ == "__main__" :
    
    """
    creer_journee_vide(27, 1, 2022, "georgesdutreux@ambulance_des_estuaires.fr")
    """
    
    """
    journee_existe_pour_ce_medecin(27, 1, 2022, "georgesdutreux@ambulance_des_estuaires.fr")
    """
    
    """
    passer_creneau_dispo_en_creneau_pris(27, 1, 2022, 10, 30, "georgesdutreux@ambulance_des_estuaires.fr")
    """
    
    """
    rdv_dispo(27, 1, 2022, 10, 30, "georgesdutreux@ambulance_des_estuaires.fr")
    """
    
    """
    temps_motif("generaliste", "checkup standard")
    """
    
    """
    temps_motif("generaliste", "checkup standard")
    """
    
    """
    passer_rdv_dispo_en_rdv_pris(27, 1, 2022, 13, 30, "georgesdutreux@ambulance_des_estuaires.fr", 60)
    """
    
    """
    creneau_possible_max(27, 1, 2022, 8, 15, "georgesdutreux@ambulance_des_estuaires.fr")
    """
    
    """
    rdv_disponible(27, 1, 2022, "georgesdutreux@ambulance_des_estuaires.fr", 60)
    """
    
    """
    medecins_disponibilites_avec_localisation("generaliste", "checkup standard", "LE-HAVRE", 27, 1, 2022)
    """
    
    """
    profil_medecin_complet("Dr Georges Dutreux")
    """
    
    #toutes les fonctions presentes ici sont testees et fonctionnent correctement