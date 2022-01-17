from errno import ECANCELED
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

                clef_valide = echanges_donnees.reception(socket) #Le serveur renvoie la validité de la clef de connexion du patient

            else: #Le client choisit de créer un compte
                launcher.sequence('Yp',[0,0]) #TODO supprimer argument inutile
                #On récupère les données fournies par le patient lors de son inscription del'IHM
                envoi_donnees_inscription = '02pCREACOMPTE'
                nom_patient = fonctions.Inom()
                prenom_patient = fonctions.Iprenom()
                jour_naiss_patient,mois_naiss_patient,annee_naiss_patient = fonctions.Ijour(),fonctions.Imois(),fonctions.Iannee()
                date_naissance_patient = jour_naiss_patient + "/" + mois_naiss_patient + "/" + annee_naiss_patient
                date_naissance_patient = date_naissance_patient
                numero_patient = fonctions.Inumero()
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                #On envoie les données fournies par le patient lors de son inscription pour l'inscrire dans la bdd côté serveur
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
        if confirmation_serveur == '03pINITPRISERDV': #Le serveur valide le lancement de la fenêtre de prise de rdv
            str_dico_type_rdv = echanges_donnees.reception(socket) #On réceptionne depuis le serveur le dictionnaire sous form d'un string nécessaire au foncionnement de l'IHM de prise de rdv
            dico_type_rdv = conversion_types.from_string_to_dict(str_dico_type_rdv) #On le convertit effectivement en dictionnaire

            launcher.sequence('IIIp',dico_type_rdv) #On lance la fenêtre de prise de rdv
            #On réceptionne les conditions du rdv choisies par le patient
            localisation = fonctions.Clocation()
            type_docteur = fonctions.Cpraticien()
            type_rdv = fonctions.CRdV()
            date_rdv = fonctions.Cjour() + "/" + fonctions.Cmois() + "/" + fonctions.Cannee()
            date_rdv = date_rdv

            envoi_donnees_prise_rdv = '03pSENDDATARDV' #On signale au serveur que le patient a effectivement saisi ses conditions de rdv
            echanges_donnees.envoi(socket,envoi_donnees_prise_rdv)
            echanges_donnees.envoi(socket,localisation) #On envoie les conditions du patient au serveur
            echanges_donnees.envoi(socket,type_docteur)
            echanges_donnees.envoi(socket,type_rdv)
            echanges_donnees.envoi(socket,date_rdv)
        else: #Si le serveur ne valide pas le lancement de la fenêtre de prise de rdv, c'est une erreur, le client s'arrête donc
            raise NotImplementedError

        confirmation_serveur = echanges_donnees.reception(socket) #Le serveur indique s'il y a des rdvs dispos ou non sous ces conditions

        if confirmation_serveur == '04pINITAFFDISPO': #Le serveur confirme qu'il existe des rdvs dispos sous ces conditions
            str_dico_disponibilites = echanges_donnees.reception(socket) #On réceptionne sous forme d'un string le dictionnaire permettant l'affichage des rdvs dispos
            dico_disponibilites = conversion_types.from_string_to_dict(str_dico_disponibilites) #One le convertit effectivement sous la forme d'un dictionnaore

            launcher.sequence('IVp',(dico_disponibilites, rdv_non_dispo)) #On lance la fenêtre d'affichage des rdvs dispos avec un booléen pour afficher s'il n'y pas de rdvs dispos sous les conditions remplies par le patient
            
            if True: #Si le rdv est validé par le patient
                envoi_validation_rdv = '04pVALIDATIONRDV' #Confirmation au serveur que le patient a bien validé un rdv
                #On réceptionne les données validées par le patient
                nom_docteur_rdv_choisi = fonctions.Ddocname()
                horaire_rdv_choisi = fonctions.DHoraireRdv()
                infos_supp_pour_docteur = fonctions.DInfos()
                #On envoie les données au serveur
                echanges_donnees.envoi(socket,envoi_validation_rdv)
                echanges_donnees.envoi(socket,nom_docteur_rdv_choisi)
                echanges_donnees.envoi(socket,horaire_rdv_choisi)
                echanges_donnees.envoi(socket,infos_supp_pour_docteur)
                rdv_validé = True #Le rdv est donc bien validé

            else: #Si un rdv n'est pas validé par le patient c'est un erreur, le client se ferme
                raise NotImplementedError

        elif confirmation_serveur == '04pRDVNONDISPO': #S'il n'y a pas de rdv dispo pour ces conditions, on revient au début de la boucle
            rdv_validé = False #Le rdv n'est donc pas validé
            rdv_non_dispo = True #Il n'y a donc pas de rdv dispo sous les conditons saisies par le patient
        else: #Si le serveur renvoie autre chose que l'information qu'il existe ou non des rdvs dispos sous les conditions du patient, c'est un erreur, le client s'arrête donc
            raise NotImplementedError

    confirmation_serveur = echanges_donnees.reception(socket) #On attend la validation du serveur pour démarrer la fenêtre récapitulative du rdv une fois celui-ci validé
    if confirmation_serveur == 'VpINITRECAP': #Le serveur valide le lancement de la fenêtre récapitulative du rdv
        #On réceptionne les coordonnées du docteur pour la fenêtre récapitulative
        rue_docteur = echanges_donnees.reception(socket)
        ville_docteur = echanges_donnees.reception(socket)
        code_postal_docteur = echanges_donnees.reception(socket)
        telephone_docteur = echanges_donnees.reception(socket)
        mail_docteur = echanges_donnees.reception(socket)
        #On affiche la fenêtre récapitulative
        launcher.sequence('Vp',(date_rdv,horaire_rdv_choisi,nom_docteur_rdv_choisi,rue_docteur,ville_docteur,code_postal_docteur,telephone_docteur,mail_docteur,infos_supp_pour_docteur))
    else: #Si le serveur ne valide pas le lancement de la fenêtre récapitulative du rdv c'est un erreur, le client se ferme
        raise NotImplementedError