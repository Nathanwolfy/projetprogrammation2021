from . import profil as p
import sqlite3



def connection_bdd():
    """cette fonction est utile pour la partie de nathan : il fait le lien
    entre serveur et client et a donc besoin de cette fonction pour se
    connecter a la base de donnee cote serveur"""
    path = "./modules/modules_sqlite/donnees.db"
    return sqlite3.connect(path)

def connection_bdd_calendrier():
    """cette fonction possede exactement la meme utilite que la fonction
    ci dessus, la seule differenece reside dans le fichier ouvert, ici
    c'est calendrier.db"""
    path = "./modules/modules_sqlite/calendrier.db"
    return sqlite3.connect(path)


def bdd_recherche(table, string):
    """cette fonction peut servir a faciliter la fonction recherche 
    en prenant en compte toutes les tables de la base de donnees, 
    cette fonction est restee a l'etat de projet pour l'instant"""
    pass



def lire_sql_medecin(row):
    """cette fonction cree un medecin a partir de la ligne du document 
    sql"""
    doc = p.Docteur()
    doc.saisie(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    return doc

def liste_medecin():
    """cette fonction utilise la bdd sql, precisement la table medecins
    ou on met nos donnees en paramametre, elle utilise la fonction ci 
    dessus pour retourner une liste exploitale de tous les docteurs"""
    liste_praticiens = []
    connection = connection_bdd()
    cursor = connection.cursor()
    req = cursor.execute('SELECT * FROM medecins')
    for row in req.fetchall():
        doc = lire_sql_medecin(row)
        liste_praticiens.append(doc)
    connection.close()
    return liste_praticiens



def liste_type_medecin():
    """cette fonction envoie la liste sans redondance des types de medecin
    presents et pris en charge dans notre base de donnee"""
    liste_type_medecins = []
    connection = connection_bdd()
    cursor = connection.cursor()
    req = cursor.execute('SELECT DISTINCT type_de_medecin FROM rdvs')#sans redondance, se traduit ici par l'utilisation de SELECT DISTINCT
    for elt in req.fetchall():
        liste_type_medecins.append(elt[0])
    connection.close()
    return liste_type_medecins
    
def liste_rendez_vous_du_medecin(type_de_medecin):
    """cette fonction renvoie une liste des motifs de rendez vous pris 
    par ce type de medecin specifique (type_de_medecin)"""
    liste_type_rdvs = []
    connection = connection_bdd()
    cursor = connection.cursor()
    type_de_medecin_sql = (type_de_medecin,)
    req = cursor.execute('SELECT DISTINCT motif FROM rdvs WHERE type_de_medecin = ?', type_de_medecin_sql)
    for elt in req.fetchall():#encore une fois sans redondance : SELECT DISTINCT
        liste_type_rdvs.append(elt[0])
    connection.close()
    return liste_type_rdvs

def liste_type_de_medecin_et_rdv_pris():
    """cette fonction retoune une liste d'une liste de motif que pratiquent un type
    de medecin avec le meme indice que la liste de medecins"""
    liste_complete = []
    liste_type_medecins = liste_type_medecin()
    for elt in liste_type_medecins:
        liste_complete.append(liste_rendez_vous_du_medecin(elt))
    return liste_complete

def dictionnaire_pour_qt():
    """cette fonction extrait de la base de donnee les different types
    de medecins et leurs différents motifs sous la forme {'generaliste' : ['certificat medical', 'vaccin', ...], 'allergologue' : ..."""
    n = len(liste_type_medecin())
    thisdict = {}
    for i in range (n) :
        thisdict[liste_type_medecin()[i]] = liste_type_de_medecin_et_rdv_pris()[i]
    return thisdict



def lire_sql_patient(row):
    """cette fonction cree le patient à partir de la ligne de meme 
    format que les lignes de la table patients de la bdd donnees"""
    patient = p.Patient()
    date = [ int(row[2]), int(row[3]), int(row[4]) ]
    patient.saisie(row[0], row[1], row[5], row[6], date)#ordre : prenom nom mail telephone date
    return patient

def liste_patient():
    """cette fonction prends la bdd donnees ou on met nos donnees en param
    le lit et retourne une liste exploitale de tous les patients grace a 
    la fonction ci dessus"""
    liste_patients = []
    connection = connection_bdd()
    cursor = connection.cursor()
    req = cursor.execute('SELECT * FROM patients')
    for row in req.fetchall():
        patient = lire_sql_patient(row)
        liste_patients.append(patient)
    connection.close()
    return liste_patients


def mdp_existe(mail):
    """cette fonction prends un mail, regarde si il existe un login enregistre
    dans la bdd identifiants avec ce mail, si oui renvoie True, si non renvoie False, 
    cette fonction est utilisee dans exploitation_sql_patient/medecin, elle fait 
    partie des choses que j'ai reussi a mutualiser"""
    connection = connection_bdd()
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
    liste_personnes_malades = liste_patient()
    print(liste_personnes_malades)
    """
    
    """
    print(mdp_existe("georgesdutreux@ambulance_des_estuaires.fr"))
    """
    
    """
    print (liste_type_medecin())
    """

    """
    print (liste_rendez_vous_du_medecin("generaliste"))
    """
    
    """
    print (liste_type_de_medecin_et_rdv_pris())
    """
    
    """
    print (dictionnaire_pour_qt())
    """
    
    """
    str_dico = str(dictionnaire_pour_qt())
    from_string_to_dict(str_dico)
    """
    
    #Toutes les fonctions semblent fonctionner correctement