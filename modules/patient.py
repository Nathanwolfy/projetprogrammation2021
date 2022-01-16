import sys

from .IHM.IHM_en_Python import launcher, fonctions
from . import fonctions_transfert
from . import echanges_donnees

FORMAT = 'utf-8'

def client_patient(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas d'identifiant saisi au départ
    while clef_valide == 'False':
        confirmation_serveur = echanges_donnees.reception(socket)
        
        if confirmation_serveur == '02pINITCONN':
            launcher.sequence('IIg',identifiant)
            creationcompte_patient = fonctions.Bcreationcompte()
                        
            if not creationcompte_patient: #Le client choisit de rentrer son identifiant et mot de passe
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentrés par le client
                clef_patient = clef_patient

                envoi_clef_connexion = '02pSENDCLEF'
                echanges_donnees.envoi(socket,envoi_clef_connexion)
                echanges_donnees.envoi(socket,clef_patient)

                clef_valide = echanges_donnees.reception(socket)

            else: #Le client choisit de créer un compte
                launcher.sequence('Yp',[0,0])
                envoi_donnees_inscription_debut = 'YYpINITSENDDATA'
                nom_patient = fonctions.Inom()
                prenom_patient = fonctions.Iprenom()
                jour_naiss_patient,mois_naiss_patient,annee_naiss_patient = fonctions.Ijour(),fonctions.Imois(),fonctions.Iannee()
                date_naissance_patient = jour_naiss_patient + "/" + mois_naiss_patient + "/" + annee_naiss_patient
                date_naissance_patient = date_naissance_patient
                numero_patient = fonctions.Inumero()
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                envoi_donnees_inscription_fin = 'YYpTERMSENDDATA'

                echanges_donnees.envoi(socket,envoi_donnees_inscription_debut)
                echanges_donnees.envoi(socket,nom_patient)
                echanges_donnees.envoi(socket,prenom_patient)
                echanges_donnees.envoi(socket,date_naissance_patient)
                echanges_donnees.envoi(socket,numero_patient)
                echanges_donnees.envoi(socket,identifiant)
                echanges_donnees.envoi(socket,motdepasse)
                echanges_donnees.envoi(socket,envoi_donnees_inscription_fin)
                clef_valide = 'True' #Le client a créé son compte, il est donc bien identifié
                
        else:
            raise NotImplementedError

    rdv_validé = False
    rdv_non_dispo = False
    while not rdv_validé:
        confirmation_serveur = echanges_donnees.reception(socket)

        if confirmation_serveur == '03pINITPRISERDV':
            str_dico_type_rdv = echanges_donnees.reception(socket)
            dico_type_rdv = fonctions_transfert.from_string_to_dict(str_dico_type_rdv)

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
            dico_disponibilites = fonctions_transfert.from_string_to_dict(str_dico_disponibilites)

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