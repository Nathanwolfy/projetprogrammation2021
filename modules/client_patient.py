import sys

from .modules_IHM.IHM_en_Python import launcher, fonctions
from .modules_echanges import conversion_types
from .modules_echanges import echanges_donnees

def client_patient(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas d'identifiant saisi au départ
    while clef_valide == 'False': #Tant que la clef n'est pas valide on relance la fenêtre de connexion
        confirmation_serveur = echanges_donnees.reception(socket) #On attend la validation du serveur pour lancer la connexion
        
        if confirmation_serveur == '02pINITCONN': #Le serveur valide de lancement de la fenêtre de connexion
            launcher.sequence('IIg',identifiant) #On lance la fenêtre de connexion
            creationcompte_patient = fonctions.Bcreationcompte() #On récupère un booléen pour savoir si le patient se connecte ou non
                        
            if not creationcompte_patient: #Le client choisit de rentrer son identifiant et mot de passe
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentrés par le client
                clef_patient = clef_patient

                envoi_clef_connexion = '02pSENDCLEF' #On envoie la réponse comme quoi le docteur se connecte et sa clef (mail+mdp) de connexion saisie
                echanges_donnees.envoi(socket,envoi_clef_connexion)
                echanges_donnees.envoi(socket,clef_patient)

                clef_valide = echanges_donnees.reception(socket)

            else: #Le client choisit de créer un compte
                launcher.sequence('Yp',[0,0]) #TODO supprimer argument inutile
                #On récupère les données fournies par le patient lors de son inscription
                envoi_donnees_inscription = '02pCREACOMPTE'
                nom_patient = fonctions.Inom()
                prenom_patient = fonctions.Iprenom()
                jour_naiss_patient,mois_naiss_patient,annee_naiss_patient = fonctions.Ijour(),fonctions.Imois(),fonctions.Iannee()
                date_naissance_patient = jour_naiss_patient + "/" + mois_naiss_patient + "/" + annee_naiss_patient
                date_naissance_patient = date_naissance_patient
                numero_patient = fonctions.Inumero()
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()

                echanges_donnees.envoi(socket,envoi_donnees_inscription)
                echanges_donnees.envoi(socket,nom_patient)
                echanges_donnees.envoi(socket,prenom_patient)
                echanges_donnees.envoi(socket,date_naissance_patient)
                echanges_donnees.envoi(socket,numero_patient)
                echanges_donnees.envoi(socket,identifiant)
                echanges_donnees.envoi(socket,motdepasse)
                clef_valide = 'True' #Le client a créé son compte, il est donc bien identifié
                
        else: #Si le serveur de valide pas le lancement de la fenêtre de connexion, l'application s'arrête
            raise NotImplementedError

    rdv_validé = False #On établit que le client n'a pas encore validé de rdv
    rdv_non_dispo = False #On établit qu'il n'y a pas de rdv dispos sous ces conditions
    while not rdv_validé:
        confirmation_serveur = echanges_donnees.reception(socket) #On attend la validation du serveur pour lancer la fenêtre de prise de rdv
        print(confirmation_serveur)
        if confirmation_serveur == '03pINITPRISERDV':
            str_dico_type_rdv = echanges_donnees.reception(socket)
            dico_type_rdv = conversion_types.from_string_to_dict(str_dico_type_rdv)

            launcher.sequence('IIIp',dico_type_rdv)
            localisation = fonctions.Clocation()
            type_docteur = fonctions.Cpraticien()
            type_rdv = fonctions.CRdV()
            date_rdv = fonctions.Cjour() + "/" + fonctions.Cmois() + "/" + fonctions.Cannee()
            date_rdv = date_rdv

            envoi_donnees_prise_rdv = '03pSENDDATARDV'
            echanges_donnees.envoi(socket,envoi_donnees_prise_rdv)

            echanges_donnees.envoi(socket,localisation)
            echanges_donnees.envoi(socket,type_docteur)
            echanges_donnees.envoi(socket,type_rdv)
            echanges_donnees.envoi(socket,date_rdv)
        else: 
            raise NotImplementedError

        confirmation_serveur = echanges_donnees.reception(socket)

        if confirmation_serveur == '04pINITAFFDISPO':
            str_dico_disponibilites = echanges_donnees.reception(socket)
            dico_disponibilites = conversion_types.from_string_to_dict(str_dico_disponibilites)

            launcher.sequence('IVp',(dico_disponibilites))
            
            if True: #Si le rdv est validé
                envoi_validation_rdv = '04pVALIDATIONRDV'
 #Confirmation au serveur qu'on valide le rdv et envoi des infos correspondantes
                nom_docteur_rdv_choisi = fonctions.Ddocname()

                horaire_rdv_choisi = fonctions.DHoraireRdv()

                infos_supp_pour_docteur = fonctions.DInfos()


                echanges_donnees.envoi(socket,envoi_validation_rdv)
                echanges_donnees.envoi(socket,nom_docteur_rdv_choisi)
                echanges_donnees.envoi(socket,horaire_rdv_choisi)
                echanges_donnees.envoi(socket,infos_supp_pour_docteur)
                rdv_validé = True
            elif False: #Retour en arrière
                pass
            else: #Fermeture de fenêtre
                #TODO envoi de code en cas de fermeture de fenêtre
                sys.exit()
                pass

        elif confirmation_serveur == '04pRDVNONDISPO': #S'il n'y a pas de rdv dispo pour ces conditions, on revient au début de la boucle
            rdv_validé = False
            rdv_non_dispo = True
        else:
            raise NotImplementedError

    confirmation_serveur = echanges_donnees.reception(socket)
    if confirmation_serveur == 'VpINITRECAP':
        launcher.sequence('Vp',(date_rdv,horaire_rdv_choisi,nom_docteur_rdv_choisi,'rue à remplir','ville à remplir','code postal à remplir','numéro à remplir','adresse email à remplir',infos_supp_pour_docteur))
    else:
        raise NotImplementedError

    sys.exit()