from ast import Not
from os import error
''' Ce fichier créer la classe dont une instance sera créée pour chaque nouveau client connecté.
Il détaille dans la méthode 'run' toutes les actions que le serveur devra effectué quand un client se connecte.
Du côté client seule la réception de la requête de choix sera identique entre patient et docteur.
'''

import threading
from .modules_sqlite import exploitation_sql_patient,exploitation_sql_medecin,lire_sql, rdv_dispo_pris, construction_edt, edt_medecin_vide
from .modules_echanges import echanges_donnees, conversion_types, types_exception

FORMAT = 'utf-8'

# Création de la classe pour les threads

class ThreadForServer(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn #On donne au thread l'adresse de connexion en argument

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

                #On réceptionne le signal d'envoi des clés de connexion ou de création de compte
                reponse = echanges_donnees.reception(self.conn)
                

                if reponse == '02pSENDCLEF': #Le patient choisit d'envoyer sa clé de connexion
                    clef_connexion = echanges_donnees.reception(self.conn).split(" ") #On réceptionne la clef de connexion (email espacé d'un espace du mdp)
                    identifiant_patient, hash_motdepasse_patient = clef_connexion[0], clef_connexion[1]

                    if identifiant_patient == 'NULL': #Dans le cas où aucun email n'a été rentré, la clef est forcément fausse
                        clef_valide = 'False'

                    else: #Si ce n'est pas le cas, le processus suit son cours
                        clef_valide = str(exploitation_sql_patient.connexion_patient_reussie(identifiant_patient,hash_motdepasse_patient)) #On vérifie que la clef de connexion est valide
                    
                    echanges_donnees.envoi(self.conn,clef_valide) #On envoie le résultat de l'évaluation de la validité de la clef de connexion

                elif reponse == '02pCREACOMPTE': #Le patient choisit de créer un compte
                    #On réceptionne toutes les informations lors de la création du compte du patient
                    nom_patient = echanges_donnees.reception(self.conn)
                    prenom_patient = echanges_donnees.reception(self.conn)
                    date_naissance_patient = echanges_donnees.reception(self.conn)
                    numero_patient = echanges_donnees.reception(self.conn)
                    identifiant_patient = echanges_donnees.reception(self.conn)
                    hash_motdepasse_patient = echanges_donnees.reception(self.conn)
                    jour_naiss_patient,mois_naiss_patient,annee_naiss_patient=date_naissance_patient.split('/')
                    
                    #On inscrit effectivement le patient dans la base de données
                    exploitation_sql_patient.inscription_patient(prenom_patient,nom_patient,jour_naiss_patient,mois_naiss_patient,annee_naiss_patient,identifiant_patient,numero_patient,hash_motdepasse_patient,hash_motdepasse_patient)
                    clef_valide = 'True' #Le patient s'est créé un compte, il est donc bien connecté
                
                elif reponse == '02pINVALIDDATA': #Si le patient rentre une donnée invalide, son inscription n'est pas validée
                    clef_valide = 'False'

                elif reponse == 'XXgKILLTHREAD':
                    raise types_exception.ClientDisconnectedError

                else: #Si le client renvoie autre chose, c'est une erreur, le thread s'arrête
                    raise types_exception.InvalidClientReponseError

            #On initie la suite la prise de rdv
            dico_type_rdv = str(lire_sql.dictionnaire_pour_qt()) #On réceptionne depuis la base de donnée le dictionnaire nécessaire au foncionnement de l'IHM de prise de rdv
            rdv_validé = False #On établit que le rdv n'est pas validé pour relancer la démarche tant qu'il ne l'est pas
            while not rdv_validé:
                code_initialisation_prise_rdv = '03pINITPRISERDV' #Le serveur valide l'initialisation de la prise du rdv
                echanges_donnees.envoi(self.conn,code_initialisation_prise_rdv)
                echanges_donnees.envoi(self.conn,dico_type_rdv) #On envoie la dictionnaire pour l'IHM
                
                reponse = echanges_donnees.reception(self.conn) #Le serveur attend la décision du client

                if reponse == '03pSENDDATARDV': #Le client confirme que le patient a choisi les conditions de son rdv
                    #Le serveur réceptionne les conditions souhaitées par le patient pour son rdv
                    localisation = echanges_donnees.reception(self.conn)
                    type_docteur = echanges_donnees.reception(self.conn)
                    type_rdv = echanges_donnees.reception(self.conn)
                    date_rdv = echanges_donnees.reception(self.conn)
                    jour,mois,annee = date_rdv.split('/')
                    
                    #Le serveur récupère de la base de données les disponibilités selon les conditions
                    dico_disponibilités = str(rdv_dispo_pris.medecins_disponibilites_avec_localisation(type_docteur,type_rdv,localisation,jour,mois,annee))

                    if dico_disponibilités != '{}': #S'il existe des rdvs dispo sous ces conditions
                        code_initialisation_affichage_disponibilites = '04pINITAFFDISPO' #On initialise l'affichage des disponibilités

                        echanges_donnees.envoi(self.conn,code_initialisation_affichage_disponibilites) #Le serveur envoie successivement la validation qu'il existe des rdvs sous ces conditions et les disponibilités
                        echanges_donnees.envoi(self.conn,dico_disponibilités)

                        reponse_patient = echanges_donnees.reception(self.conn) #Le serveur attend la décision du patient

                        if reponse_patient == '04pVALIDATIONRDV': #Le patient valide son rdv
                            #On réceptionne le nom du docteur, l'horaire et les notes pour le docteur suite à la validation du rdv
                            nom_docteur_choisi_rdv = echanges_donnees.reception(self.conn)
                            horaire_rdv_choisi = echanges_donnees.reception(self.conn).split(':')
                            notes_pour_docteur = echanges_donnees.reception(self.conn)
                            heure = str(horaire_rdv_choisi[0])
                            minute = str(horaire_rdv_choisi[1])
                            
                            construction_edt.construction_edt(nom_docteur_choisi_rdv, jour, mois, annee, heure, minute, type_rdv, notes_pour_docteur) #On ajoute le rdv dans la base de données
                            rdv_validé = True #Le rdv est effectivement validé

                        elif reponse_patient == 'XXgKILLTHREAD': #Dans le cas où le client ferme la fenêtre
                            raise types_exception.ClientDisconnectedError

                        else: #Dans le cas où le client renvoie autre chose, c'est un erreur
                            raise types_exception.InvalidClientReponseError

                    else: #S'il n'y a pas de rdv dispos sous ces conditions, on revient au début de la boucle
                        code_initialisation_affichage_disponibilites = '04pRDVNONDISPO' #On confirme au patient qu'il n'existe pas de rdv dispo sous ces conditions
                        echanges_donnees.envoi(self.conn,code_initialisation_affichage_disponibilites)
                        rdv_validé = False #Le rdv n'est pas validé

                elif reponse == '03pINVALIDDATA': #Dans le cas où le patient n'a pas rentré toutes les données
                    code_initialisation_affichage_disponibilites = '04pRDVNONDISPO' #On confirme au patient qu'il n'existe pas de rdv dispo sous ces conditions
                    echanges_donnees.envoi(self.conn,code_initialisation_affichage_disponibilites)
                    rdv_validé = False #Le rdv n'est pas validé

                elif reponse == 'XXgKILLTHREAD': #Dans le cas où le client ferme la fenêtre
                    raise types_exception.ClientDisconnectedError 

                else: #Si le client renvoie autre chose, c'est une erreur, le thread s'arrête
                    raise types_exception.InvalidClientReponseError

            #On initie le récap des informations
            code_initialisation_recap_patient = 'VpINITRECAP'
            #On réceptionne les coordonnées du docteur pour le patient depuis la base de données
            coordonnées_docteur = rdv_dispo_pris.profil_medecin_complet(nom_docteur_choisi_rdv)
            rue_docteur = coordonnées_docteur[2]
            ville_docteur = coordonnées_docteur[4]
            code_postal_docteur = coordonnées_docteur[3]
            telephone_docteur = coordonnées_docteur[1]
            mail_docteur = coordonnées_docteur[0]
            #On envoie l'initialisation du récap du patient ainsi que les données nécessaires
            echanges_donnees.envoi(self.conn,code_initialisation_recap_patient)
            echanges_donnees.envoi(self.conn,rue_docteur)
            echanges_donnees.envoi(self.conn,ville_docteur)
            echanges_donnees.envoi(self.conn,code_postal_docteur)
            echanges_donnees.envoi(self.conn,telephone_docteur)
            echanges_donnees.envoi(self.conn,mail_docteur)
            #Une fois l'initialisation du récap et les données envoyées, le thread peut s'arrêter

        elif choix_client == 'XXd': #Le client choisi est celui du docteur
            
            clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas.
            while clef_valide == 'False':
                code_initialisation_connexion_docteur = '02dINITCONN'
                echanges_donnees.envoi(self.conn,code_initialisation_connexion_docteur)

                #On réceptionne le signal d'envoi des clés de connexion
                reponse = echanges_donnees.reception(self.conn)    

                if reponse == '02dSENDCLEF': #Le docteur choisit d'envoyer sa clé de connexion
                    clef_connexion = echanges_donnees.reception(self.conn).split(" ")
                    identifiant_docteur, hash_motdepasse_docteur = clef_connexion[0], clef_connexion[1]

                    if identifiant_docteur == 'NULL': #Dans le cas où aucun email n'a été rentré, la clef est forcément fausse
                        clef_valide = 'False'

                    else: #Si ce n'est pas le cas, le processus suit son cours
                        clef_valide = str(exploitation_sql_medecin.connexion_medecin_reussie(identifiant_docteur,hash_motdepasse_docteur)) #On vérifie que la clef de connexion est valide

                    echanges_donnees.envoi(self.conn,clef_valide)

                elif reponse == '02dCREACOMPTE': #Le docteur choisir de créer son compte
                    str_liste_types_docteur = str(lire_sql.liste_type_medecin()) #Le serveur envoie la liste des types de médecins
                    echanges_donnees.envoi(self.conn,str_liste_types_docteur)
                    #On réceptionne les données saisies par le docteur lors de son inscription
                    nom_docteur = echanges_donnees.reception(self.conn)
                    prenom_docteur = echanges_donnees.reception(self.conn)
                    type_docteur = echanges_donnees.reception(self.conn)
                    ville_docteur = echanges_donnees.reception(self.conn)
                    rue_docteur = echanges_donnees.reception(self.conn)
                    code_postal_docteur = echanges_donnees.reception(self.conn)
                    telephone_docteur = echanges_donnees.reception(self.conn)
                    identifiant_docteur = echanges_donnees.reception(self.conn)
                    hash_motdepasse_docteur = echanges_donnees.reception(self.conn)
                    #On inscrit effecivement le docteur dans la base de données
                    exploitation_sql_medecin.inscription_medecin(prenom_docteur,nom_docteur,type_docteur,identifiant_docteur,telephone_docteur,rue_docteur,code_postal_docteur, ville_docteur,hash_motdepasse_docteur,hash_motdepasse_docteur)

                    code_initialisation_inscription_edt_docteur = '02dINITINSCEDTDOC' #On valide au client le lancement de la fenêtre d'inscription de l'edt du docteur
                    echanges_donnees.envoi(self.conn, code_initialisation_inscription_edt_docteur)
                    #On réceptionne une string représentant une liste des horaires de début et de fin pour chaque jour, on les convertit directement en liste de deux string
                    horaire_lundi = conversion_types.strlist_to_list(echanges_donnees.reception(self.conn))
                    horaire_mardi = conversion_types.strlist_to_list(echanges_donnees.reception(self.conn))
                    horaire_mercredi = conversion_types.strlist_to_list(echanges_donnees.reception(self.conn))
                    horaire_jeudi = conversion_types.strlist_to_list(echanges_donnees.reception(self.conn))
                    horaire_vendredi = conversion_types.strlist_to_list(echanges_donnees.reception(self.conn))
                    horaire_samedi = conversion_types.strlist_to_list(echanges_donnees.reception(self.conn))
                    #On inscrit les rdv disponibles inscrits par le médecin dans la bdd
                    edt_medecin_vide.edt_medecin_vide(identifiant_docteur,horaire_lundi, horaire_mardi, horaire_mercredi, horaire_jeudi, horaire_vendredi, horaire_samedi)

                    clef_valide = 'True' #Le docteur vient de se créer un compte, il est donc bien connecté

                elif reponse == '02dINVALIDDATA': #Si le docteur rentre une donnée invalide, son inscription n'est pas validée
                    clef_valide = 'False'
                
                elif reponse == 'XXgKILLTHREAD': #Dans le cas où le client ferme la fenêtre
                    raise types_exception.ClientDisconnectedError

                else: #Dans le cas où le client renvoie autre chose, c'est un erreur
                    raise types_exception.InvalidClientReponseError

        elif choix_client == 'XXgKILLTHREAD': #Dans le cas où le client ferme la fenêtre
            raise types_exception.ClientDisconnectedError

        else: #Si le client ne choisit pas le client docteur ou patient c'est une erreyr, le thread s'arrête
            raise types_exception.InvalidClientReponseError