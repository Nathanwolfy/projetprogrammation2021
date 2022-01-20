from .modules_echanges import conversion_types

from .modules_IHM.IHM_en_Python import launcher
from .modules_echanges import echanges_donnees, types_exception, hashage_mdp, stop_continuation

def client_docteur(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas d'identifiant saisi au départ
    while clef_valide == 'False': #Tant que la clef n'est pas valide on relance la fenêtre de connexion
        confirmation_serveur = echanges_donnees.reception(socket) #On attend la validation du serveur pour lancer la connexion
        
        if confirmation_serveur == '02dINITCONN':
            fenetre_connexion_docteur = launcher.Bconnexionouinscription_herit(identifiant)
            launcher.exec_fenetre(fenetre_connexion_docteur) #On démarre la fenêtre de connexion avec un identifiant prélablement rempli par le docteur si mauvaise combinaison
            creationcompte_docteur = fenetre_connexion_docteur.creation_compte
            continuation = fenetre_connexion_docteur.continuation

            if not continuation: #Si le client ne clique sur aucun bouton donc ferme la fenêtre, on envoie au serveur l'indication et on termine le script client
                stop_continuation.arret_processus(socket)
                        
            elif not creationcompte_docteur: #Le client choisit de rentrer son identifiant et mot de passe
                identifiant = fenetre_connexion_docteur.identifiant_client
                hash_motdepasse = hashage_mdp.hash_mdp(fenetre_connexion_docteur.motdepasse_client)
                clef_docteur = identifiant + " " + hash_motdepasse #On récupère identifiants et mot de passe rentrés par le client
                clef_docteur = clef_docteur

                envoi_clef_connexion = '02dSENDCLEF' #On envoie la réponse comme quoi le docteur se connecte et sa clef (mail+mdp) de connexion saisie
                echanges_donnees.envoi(socket,envoi_clef_connexion)
                echanges_donnees.envoi(socket,clef_docteur)

                clef_valide = echanges_donnees.reception(socket)

            else: #Le docteur choisit de créer un compte
                requete_liste_types_docteur = '02dCREACOMPTE' #On demande la liste des types de docteurs
                echanges_donnees.envoi(socket,requete_liste_types_docteur)
                str_liste_types_docteurs = echanges_donnees.reception(socket) #On réceptionne la liste des types de docteurs sous forme d'une string
                liste_types_docteurs = conversion_types.strlist_to_list(str_liste_types_docteurs) #On la convertit effectivement en liste

                fenetre_inscription_docteur = launcher.InscriptionDoc_herit(liste_types_docteurs)
                launcher.exec_fenetre(fenetre_inscription_docteur) #On démarre la fenêtre de création de compte
                continuation = fenetre_inscription_docteur.continuation

                if not continuation: #Si le client ne clique sur aucun bouton donc ferme la fenêtre, on envoie au serveur l'indication et on termine le script client
                    stop_continuation.arret_processus(socket)

                else: #Si non, le processus se déroule normalement
                    #On récupère les informations saisies par le docteur dans l'IHM et on les envoie directement (on garde que l'identifiant du docteur car on en aura besoin par la suite)
                    identifiant = fenetre_inscription_docteur.mail_docteur

                    echanges_donnees.envoi(socket,fenetre_inscription_docteur.nom_docteur.capitalize()) #capitalize() pour mettre la première lettre du nom et prénom en majuscule et le reste en minuscule
                    echanges_donnees.envoi(socket,fenetre_inscription_docteur.prenom_docteur.capitalize())
                    echanges_donnees.envoi(socket,fenetre_inscription_docteur.type_docteur)
                    echanges_donnees.envoi(socket,fenetre_inscription_docteur.ville_docteur.upper()) #upper() car toutes les villes sont en majuscules dans la bdd
                    echanges_donnees.envoi(socket,fenetre_inscription_docteur.adresse_docteur)
                    echanges_donnees.envoi(socket,fenetre_inscription_docteur.code_postal_docteur)
                    echanges_donnees.envoi(socket,fenetre_inscription_docteur.numero_docteur)
                    echanges_donnees.envoi(socket,identifiant)
                    echanges_donnees.envoi(socket,hashage_mdp.hash_mdp(fenetre_inscription_docteur.mot_de_passe_docteur))

                    reponse = echanges_donnees.reception(socket) #On attend la validation du serveur pour l'inscription de l'emploi du temps du docteur

                    if reponse == '02dINITINSCEDTDOC': #Le serveur valide le lancement de l'inscription de l'emploi du temps du docteur
                        fenetre_inscription_edt_doc = launcher.InscriptionDocedt_herit()
                        launcher.exec_fenetre(fenetre_inscription_edt_doc) #On lance l'inscription de l'emploi du temps du docteur
                        continuation = fenetre_inscription_edt_doc.continuation

                        if not continuation: #Si le client ne clique sur aucun bouton donc ferme la fenêtre, on envoie au serveur l'indication et on termine le script client
                            stop_continuation.arret_processus(socket)

                        else: #Si non, le processus se déroule normalement
                            #On récuprère les horaires inscrit dans l'IHM par le docteur et on les envoie directement
                            echanges_donnees.envoi(socket,str(fenetre_inscription_edt_doc.lundi))
                            echanges_donnees.envoi(socket,str(fenetre_inscription_edt_doc.mardi))
                            echanges_donnees.envoi(socket,str(fenetre_inscription_edt_doc.mercredi))
                            echanges_donnees.envoi(socket,str(fenetre_inscription_edt_doc.jeudi))
                            echanges_donnees.envoi(socket,str(fenetre_inscription_edt_doc.vendredi))
                            echanges_donnees.envoi(socket,str(fenetre_inscription_edt_doc.samedi))                  

                    else: #Si le serveur renvoie autre chose, c'est une erreur, le client s'arrête
                        raise types_exception.InvalidServerReponseError

                    clef_valide = 'True' #Le docteur a créé son compte, il est donc bien identifié
                
        else: #Si le serveur de valide pas le lancement de la connexion, le programme s'arrête
            raise types_exception.InvalidServerReponseError