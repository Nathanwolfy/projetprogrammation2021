import profil as p
import sqlite3




def lire_sql_medecin(row):
    """cette fonction cree le medecin a partir du document sql"""
    doc = p.Docteur()
    doc.saisie(row[0], row[1], row[3], row[4], row[5], row[2])
    return doc


def liste_medecin():
    """cette fonction prends la bdd sql ou on met nos données en param
    le lit et retourne une liste exploitale de tous les docteurs"""
    liste_praticiens = []
    connection = sqlite3.connect("donnees.db")
    cursor = connection.cursor()
    req = cursor.execute('SELECT * FROM medecins')
    for row in req.fetchall():
        doc = lire_sql_medecin(row)
        liste_praticiens.append(doc)
    connection.close()
    return liste_praticiens


def lire_sql_patient(row):
    """cette fonction cree le patient à partir de la base de donnee patient
    de sql"""
    patient = p.Patient()
    date = [ int(row[2]), int(row[3]), int(row[4]) ]
    patient.saisie(row[0], row[1], row[5], row[6], row[7], date)
    return patient


def liste_patient():
    """cette fonction prends la bdd sql ou on met nos données en param
    le lit et retourne une liste exploitale de tous les patients"""
    liste_patients = []
    connection = sqlite3.connect("donnees.db")
    cursor = connection.cursor()
    req = cursor.execute('SELECT * FROM patients')
    for row in req.fetchall():
        patient = lire_sql_patient(row)
        liste_patients.append(patient)
    connection.close()
    return liste_patients


def mdp_existe(mail):
    """cette fonction prends un mail, regarde si il existe un login enregistre
    dans la bdd identifiants avec ce mail, si oui renvoie True, si non renvoie False"""
    connection = sqlite3.connect("donnees.db")
    cursor = connection.cursor()
    sql_mail = (str(mail),)
    cursor.execute('SELECT * FROM identifiants WHERE mail = ?', sql_mail)
    login_qui_existe_deja = cursor.fetchone()
    connection.close()
    return login_qui_existe_deja != None


if __name__ == "__main__" :
    
    """
    liste_paticiens = liste_medecin()
    print(liste_paticiens)
    """

    """
    liste_malades = liste_patient()
    print(liste_malades)
    """
