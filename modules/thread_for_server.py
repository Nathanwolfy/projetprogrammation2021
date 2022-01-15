from os import error
''' Ce fichier créer la classe dont une instance sera créée pour chaque nouveau client connecté.
Il détaille dans la méthode 'run' toutes les actions que le serveur devra effectué quand un client se connecte.
Du côté client seule la réception de la requête de choix sera identique entre patient et docteur.
'''

import threading
from .modules_sqlite import exploitation_sql_patient,exploitation_sql_medecin,lire_sql,exploitation_sql_rendez_vous, rdv_dispo_pris

FORMAT = 'utf-8'

# Création de la classe pour les threads

class ThreadForServer(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def initialisation_choix_client(self): #On lance la requête pour connaître le choix du client souhaité
        code_initialisation_choix_client = '01gINITCHOIX'.encode(FORMAT) 
        self.conn.sendall(code_initialisation_choix_client)

    def run(self): #Actions à faire au démarrage du Thread
        self.initialisation_choix_client() #On initialise la demande de choix du client
        choix_client = self.conn.recv(8)
        choix_client = choix_client.decode(FORMAT)

        #On lance l'initialisation de l'interface en fonction du choix de client et on déroule les étapes
        if choix_client == 'XXp':
            clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas.
            while clef_valide == 'False':
                code_initialisation_connexion_patient = '02pINITCONN'.encode(FORMAT) 
                self.conn.sendall(code_initialisation_connexion_patient)

                #On réceptionne le signal d'envoi des clés de connexion
                reponse = self.conn.recv(32)
                reponse = reponse.decode(FORMAT)

                if reponse == '02pSENDCLEF': #Le patient choisit d'envoyer sa clé de connexion
                    clef_connexion = self.conn.recv(64)
                    clef_connexion = clef_connexion.decode(FORMAT).split(" ")
                    identifiant_patient, motdepasse_patient = clef_connexion[0], clef_connexion[1]
                    
                    clef_valide = str(exploitation_sql_patient.connexion_patient_reussie(identifiant_patient,motdepasse_patient)) #On vérifie que la clef de connexion est valide
                    validation = clef_valide.encode(FORMAT)
                    self.conn.sendall(validation)

                elif reponse == 'YYpSENDDATA':
                    nom_patient = self.conn.recv(32).decode(FORMAT)
                    prenom_patient = self.conn.recv(32).decode(FORMAT)
                    date_naissance_patient = self.conn.recv(16).decode(FORMAT)
                    numero_patient = self.conn.recv(16).decode(FORMAT)
                    identifiant_patient = self.conn.recv(64).decode(FORMAT)
                    motdepasse_patient = self.conn.recv(32).decode(FORMAT)
                    jour_naiss_patient,mois_naiss_patient,annee_naiss_patient=date_naissance_patient.split('/')
                    reponse = self.conn.recv(16).decode(FORMAT)
                    if reponse == 'YYpTERMSENDDATA':
                        exploitation_sql_patient.inscription_patient(prenom_patient,nom_patient,jour_naiss_patient,mois_naiss_patient,annee_naiss_patient,identifiant_patient,numero_patient,motdepasse_patient)
                        clef_valide = 'True'
                    else:
                        raise NotImplementedError

                else:
                    raise NotImplementedError

            #On initie la suite la prise de rdv
            dico_type_rdv = str(lire_sql.dictionnaire_pour_qt()).encode(FORMAT)
            rdv_validé = False
            while not rdv_validé:
                code_initialisation_prise_rdv = '03pINITPRISERDV'.encode(FORMAT)
                self.conn.sendall(code_initialisation_prise_rdv)
                self.conn.sendall(dico_type_rdv)

                reponse = self.conn.recv(32)
                reponse = reponse.decode(FORMAT)

                if reponse == '03pSENDDATARDV':

                    localisation = self.conn.recv(32).decode(FORMAT)
                    type_docteur = self.conn.recv(32).decode(FORMAT)
                    type_rdv = self.conn.recv(32).decode(FORMAT)
                    date_rdv = self.conn.recv(16).decode(FORMAT)
                    jour,mois,annee = date_rdv.split('/')
                    
                    dico_disponibilités = str(rdv_dispo_pris.medecins_disponibilites_avec_localisation(type_docteur,type_rdv,localisation,jour,mois,annee)).encode(FORMAT)

                    if dico_disponibilités != '{}': #S'il existe des rdvs dispo sous ces conditions
                        code_initialisation_affichage_disponibilites = '04pINITAFFDISPO'.encode(FORMAT) #On initialise l'affichage des disponibilités

                        self.conn.sendall(code_initialisation_affichage_disponibilites)
                        self.conn.sendall(dico_disponibilités)

                        reponse_patient = self.conn.recv(16).decode(FORMAT)

                        if reponse_patient == '04pVALIDATIONRDV':
                            nom_docteur_choisi_rdv = self.conn.recv(32).decode(FORMAT)
                            horaire_rdv_choisi = self.conn.recv(32).decode(FORMAT)
                            notes_pour_docteur = self.conn.recv(64).decode(FORMAT)
                            #TODO valider le rdv dans la base de données avec les notes associées
                            rdv_validé = True
                        elif False: #Dans le cas où le client revient en arrière
                            pass
                        else: #Dans le cas où le client ferme la fenêtre
                            pass

                    else: #S'il n'y a pas de rdv dispos sous ces conditions, on revient au début de la boucle
                        code_initialisation_affichage_disponibilites = '04pRDVNONDISPO'.encode(FORMAT)
                        self.conn.sendall(code_initialisation_affichage_disponibilites)
                        
                else:
                    raise NotImplementedError

            #On initie le récap des informations
            code_initialisation_recap_patient = 'VpINITRECAP'.encode(FORMAT)
            self.conn.sendall(code_initialisation_recap_patient)
            #TODO envoyer adresse, numéro de téléphone et email du docteur au patient
            #Une fois l'initialisation du récap envoyée, le thread peut s'arrêter

        elif choix_client == 'XXd':
            code_initialisation_connexion_docteur = '02dINITCONN'.encode(FORMAT)
            self.conn.sendall(code_initialisation_connexion_docteur)
        else:
            pass
            #raise NotImplementedError ?