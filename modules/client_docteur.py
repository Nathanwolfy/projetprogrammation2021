from .modules_echanges import conversion_types

from .modules_IHM.IHM_en_Python import launcher, fonctions
from .modules_echanges import echanges_donnees

def client_docteur(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas d'identifiant saisi au départ
    while clef_valide == 'False': #Tant que la clef n'est pas valide on relance la fenêtre de connexion
        confirmation_serveur = echanges_donnees.reception(socket) #On attend la validation du serveur pour lancer la connexion
        
        if confirmation_serveur == '02dINITCONN':
            launcher.sequence('IIg',identifiant) #On démarre la fenêtre de connexion avec un identifiant prélablement rempli par le docteur si mauvaise combinaison
            creationcompte_patient = fonctions.Bcreationcompte()
                        
            if not creationcompte_patient: #Le client choisit de rentrer son identifiant et mot de passe
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentrés par le client
                clef_patient = clef_patient

                envoi_clef_connexion = '02dSENDCLEF' #On envoie la réponse comme quoi le docteur se connecte et sa clef (mail+mdp) de connexion saisie
                echanges_donnees.envoi(socket,envoi_clef_connexion)
                echanges_donnees.envoi(socket,clef_patient)

                clef_valide = echanges_donnees.reception(socket)

            else: #Le docteur choisit de créer un compte
                requete_liste_types_docteur = '02dCREACOMPTE' #On demande la liste des types de docteurs
                echanges_donnees.envoi(socket,requete_liste_types_docteur)
                str_liste_types_docteurs = echanges_donnees.reception(socket) #On réceptionne la liste des types de docteurs sous forme d'une string
                liste_types_docteurs = conversion_types.strlist_to_list(str_liste_types_docteurs) #On la convertit effectivement en liste

                launcher.sequence('Yd',liste_types_docteurs) #On démarre la fenêtre de création de compte
                
                #On récupère les informations saisies par le docteur dans l'IHM
                #TODO
                nom_docteur = ''.capitalize() #capitalize() pour mettre la première lettre du nom et prénom en majuscule et le reste en minuscule
                prenom_docteur = ''.capitalize()
                type_docteur = ''
                ville_de_pratique = ''.upper() #upper() car toutes les villes sont en majuscules dans la bdd
                adresse_docteur = ''
                code_postal_docteur = ''
                numero_docteur = ''
                identifiant = ''
                motdepasse = ''

                #On envoie les informaions saisies pas le docteur
                echanges_donnees.envoi(socket,nom_docteur)
                echanges_donnees.envoi(socket,prenom_docteur)
                echanges_donnees.envoi(socket,type_docteur)
                echanges_donnees.envoi(socket,ville_de_pratique)
                echanges_donnees.envoi(socket,adresse_docteur)
                echanges_donnees.envoi(socket,code_postal_docteur)
                echanges_donnees.envoi(socket,numero_docteur)
                echanges_donnees.envoi(socket,identifiant)
                echanges_donnees.envoi(socket,motdepasse)

                reponse = echanges_donnees.reception(socket) #On attend la validation du serveur pour l'inscription de l'emploi du temps du docteur

                if reponse == '02dINITINSCEDTDOC': #Le serveur valide le lancement de l'inscription de l'emploi du temps du docteur
                    inscription_edt_doc = launcher.sequence('') #On lance l'inscription de l'emploi du temps du docteur #TODO
                    #On récuprère les horaires inscrit dans l'IHM par le docteur et on les envoie directement
                    echanges_donnees.envoi(socket,str(inscription_edt_doc.lundi))
                    echanges_donnees.envoi(socket,str(inscription_edt_doc.mardi))
                    echanges_donnees.envoi(socket,str(inscription_edt_doc.mercredi))
                    echanges_donnees.envoi(socket,str(inscription_edt_doc.jeudi))
                    echanges_donnees.envoi(socket,str(inscription_edt_doc.vendredi))
                    echanges_donnees.envoi(socket,str(inscription_edt_doc.samedi))
                    

                else: #Si le serveur renvoie autre chose, c'est une erreur, le client s'arrête
                    raise NotImplementedError

                clef_valide = 'True' #Le docteur a créé son compte, il est donc bien identifié
                
        else: #Si le serveur de valide pas le lancement de la connexion, le programme s'arrête
            raise NotImplementedError