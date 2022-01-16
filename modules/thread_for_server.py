from os import error
''' Ce fichier créer la classe dont une instance sera créée pour chaque nouveau client connecté.
Il détaille dans la méthode 'run' toutes les actions que le serveur devra effectué quand un client se connecte.
Du côté client seule la réception de la requête de choix sera identique entre patient et docteur.
'''

import threading
from .modules_sqlite import exploitation_sql_patient,exploitation_sql_medecin,lire_sql,exploitation_sql_rendez_vous, rdv_dispo_pris
from . import echanges_donnees

FORMAT = 'utf-8'

# Création de la classe pour les threads

class ThreadForServer(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self): #Actions à faire au démarrage du Thread
        code_initialisation_choix_client = '01gINITCHOIX'
        echanges_donnees.envoi(self.conn,code_initialisation_choix_client)  #On initialise la demande de choix du client

        choix_client = echanges_donnees.reception(self.conn)

        #On lance l'initialisation de l'interface en fonction du choix de client et on déroule les étapes
        if choix_client == 'XXp':
            clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas.
            while clef_valide == 'False':
                code_initialisation_connexion_patient = '02pINITCONN' 
                echanges_donnees.envoi(self.conn,code_initialisation_connexion_patient)

                #On réceptionne le signal d'envoi des clés de connexion
                reponse = echanges_donnees.reception(self.conn)
                

                if reponse == '02pSENDCLEF': #Le patient choisit d'envoyer sa clé de connexion
                    clef_connexion = echanges_donnees.reception(self.conn).split(" ")
                    identifiant_patient, motdepasse_patient = clef_connexion[0], clef_connexion[1]
                    
                    clef_valide = str(exploitation_sql_patient.connexion_patient_reussie(identifiant_patient,motdepasse_patient)) #On vérifie que la clef de connexion est valide
                    validation = clef_valide
                    echanges_donnees.envoi(self.conn,validation)

                elif reponse == 'YYpINITSENDDATA':
                    nom_patient = echanges_donnees.reception(self.conn)
                    prenom_patient = echanges_donnees.reception(self.conn)
                    date_naissance_patient = echanges_donnees.reception(self.conn)
                    numero_patient = echanges_donnees.reception(self.conn)
                    identifiant_patient = echanges_donnees.reception(self.conn)
                    motdepasse_patient = echanges_donnees.reception(self.conn)
                    jour_naiss_patient,mois_naiss_patient,annee_naiss_patient=date_naissance_patient.split('/')
                    reponse = echanges_donnees.reception(self.conn)
                    if reponse == 'YYpTERMSENDDATA':
                        exploitation_sql_patient.inscription_patient(prenom_patient,nom_patient,jour_naiss_patient,mois_naiss_patient,annee_naiss_patient,identifiant_patient,numero_patient,motdepasse_patient,motdepasse_patient)
                        clef_valide = 'True'
                    else:
                        raise NotImplementedError

                else:
                    raise NotImplementedError

            #On initie la suite la prise de rdv
            dico_type_rdv = str(lire_sql.dictionnaire_pour_qt())
            rdv_validé = False
            while not rdv_validé:
                code_initialisation_prise_rdv = '03pINITPRISERDV'
                echanges_donnees.envoi(self.conn,code_initialisation_prise_rdv)
                echanges_donnees.envoi(self.conn,dico_type_rdv)
                
                reponse = echanges_donnees.reception(self.conn)

                if reponse == '03pSENDDATARDV':

                    localisation = echanges_donnees.reception(self.conn)
                    type_docteur = echanges_donnees.reception(self.conn)
                    type_rdv = echanges_donnees.reception(self.conn)
                    date_rdv = echanges_donnees.reception(self.conn)
                    jour,mois,annee = date_rdv.split('/')
                    
                    dico_disponibilités = str(rdv_dispo_pris.medecins_disponibilites_avec_localisation(type_docteur,type_rdv,localisation,jour,mois,annee))

                    if dico_disponibilités != b'{}': #S'il existe des rdvs dispo sous ces conditions
                        code_initialisation_affichage_disponibilites = '04pINITAFFDISPO' #On initialise l'affichage des disponibilités

                        echanges_donnees.envoi(self.conn,code_initialisation_affichage_disponibilites)
                        echanges_donnees.envoi(self.conn,dico_disponibilités)

                        reponse_patient = echanges_donnees.reception(self.conn)

                        if reponse_patient == '04pVALIDATIONRDV':
                            nom_docteur_choisi_rdv = echanges_donnees.reception(self.conn)
                            horaire_rdv_choisi = echanges_donnees.reception(self.conn)
                            notes_pour_docteur = echanges_donnees.reception(self.conn)
                            #TODO valider le rdv dans la base de données avec les notes associées
                            rdv_validé = True
                        elif False: #Dans le cas où le client revient en arrière
                            pass
                        else: #Dans le cas où le client ferme la fenêtre
                            pass

                    else: #S'il n'y a pas de rdv dispos sous ces conditions, on revient au début de la boucle
                        code_initialisation_affichage_disponibilites = '04pRDVNONDISPO'
                        echanges_donnees.envoi(self.conn,code_initialisation_affichage_disponibilites)
                        rdv_validé = False
                        
                else:
                    raise NotImplementedError

            #On initie le récap des informations
            code_initialisation_recap_patient = 'VpINITRECAP'
            echanges_donnees.envoi(self.conn,code_initialisation_recap_patient)
            #TODO envoyer adresse, numéro de téléphone et email du docteur au patient
            #Une fois l'initialisation du récap envoyée, le thread peut s'arrêter

        elif choix_client == 'XXd': #Le client choisi est celui du docteur
            
            clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas.
            while clef_valide == 'False':
                code_initialisation_connexion_docteur = '02dINITCONN'
                echanges_donnees.envoi(self.conn,code_initialisation_connexion_docteur)

                #On réceptionne le signal d'envoi des clés de connexion
                reponse = echanges_donnees.reception(self.conn)    

                if reponse == '02dSENDCLEF': #Le patient choisit d'envoyer sa clé de connexion
                    clef_connexion = echanges_donnees.reception(self.conn).split(" ")
                    identifiant_docteur, motdepasse_docteur = clef_connexion[0], clef_connexion[1]
                    
                    clef_valide = str(exploitation_sql_medecin.connexion_medecin_reussie(identifiant_docteur,motdepasse_docteur)) #On vérifie que la clef de connexion est valide
                    validation = clef_valide
                    echanges_donnees.envoi(self.conn,validation)

                elif reponse == 'YYdINITSENDDATA':
                    nom_docteur = echanges_donnees.envoi(self.conn)
                    prenom_docteur = echanges_donnees.envoi(self.conn)
                    ville_de_pratique = echanges_donnees.envoi(self.conn)
                    adresse_docteur = echanges_donnees.envoi(self.conn)
                    code_postal_docteur = echanges_donnees.envoi(self.conn)
                    numero_docteur = echanges_donnees.envoi(self.conn)
                    identifiant_docteur = echanges_donnees.envoi(self.conn)
                    motdepasse_docteur = echanges_donnees.envoi(self.conn)
                    envoi_donnees_inscription_fin = echanges_donnees.envoi(self.conn)

                    if reponse == 'YYdTERMSENDDATA':
                        exploitation_sql_medecin.inscription_medecin(prenom_docteur,nom_docteur,'',identifiant_docteur,numero_docteur,'adresse à insérer',motdepasse_docteur,motdepasse_docteur)
                        clef_valide = 'True'
                    else:
                        raise NotImplementedError

                else:
                    raise NotImplementedError
        else:
            pass
            #raise NotImplementedError ?