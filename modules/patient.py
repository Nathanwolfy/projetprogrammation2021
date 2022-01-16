import sys

from .IHM.IHM_en_Python import launcher, fonctions
from . import fonctions_transfert

FORMAT = 'utf-8'

def client_patient(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas d'identifiant saisi au départ
    while clef_valide == 'False':
        confirmation_serveur = socket.recv(32)
        confirmation_serveur = confirmation_serveur.decode(FORMAT)

        if confirmation_serveur == '02pINITCONN':
            launcher.sequence('IIg',identifiant)
            creationcompte_patient = fonctions.Bcreationcompte()
                        
            if not creationcompte_patient: #Le client choisit de rentrer son identifiant et mot de passe
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentrés par le client
                clef_patient = clef_patient.encode(FORMAT)

                envoi_clef_connexion = '02pSENDCLEF'.encode(FORMAT)
                socket.sendall(envoi_clef_connexion)
                socket.sendall(clef_patient)

                retour = socket.recv(32)
                clef_valide = retour.decode(FORMAT)

            else: #Le client choisit de créer un compte
                launcher.sequence('Yp',[0,0])
                envoi_donnees_inscription_debut = 'YYpINITSENDDATA'.encode(FORMAT)
                nom_patient = fonctions.Inom().encode(FORMAT)
                prenom_patient = fonctions.Iprenom().encode(FORMAT)
                jour_naiss_patient,mois_naiss_patient,annee_naiss_patient = fonctions.Ijour(),fonctions.Imois(),fonctions.Iannee()
                date_naissance_patient = jour_naiss_patient + "/" + mois_naiss_patient + "/" + annee_naiss_patient
                date_naissance_patient = date_naissance_patient.encode(FORMAT)
                numero_patient = fonctions.Inumero().encode(FORMAT)
                identifiant = fonctions.Bidentifiant().encode(FORMAT)
                motdepasse = fonctions.Bmotdepass().encode(FORMAT)
                envoi_donnees_inscription_fin = 'YYpTERMSENDDATA'.encode(FORMAT)

                socket.sendall(envoi_donnees_inscription_debut)
                socket.sendall(nom_patient)
                socket.sendall(prenom_patient)
                socket.sendall(date_naissance_patient)
                socket.sendall(numero_patient)
                socket.sendall(identifiant)
                socket.sendall(motdepasse)
                socket.sendall(envoi_donnees_inscription_fin)
                clef_valide = 'True' #Le client a créé son compte, il est donc bien identifié
                
        else:
            raise NotImplementedError

    rdv_validé = False
    rdv_non_dispo = False
    while not rdv_validé:
        confirmation_serveur = socket.recv(32)
        confirmation_serveur = confirmation_serveur.decode(FORMAT)

        if confirmation_serveur == '03pINITPRISERDV':
            str_dico_type_rdv = socket.recv(1024).decode(FORMAT)
            dico_type_rdv = fonctions_transfert.from_string_to_dict(str_dico_type_rdv)

            launcher.sequence('IIIp',dico_type_rdv)
            localisation = fonctions.Clocation().encode(FORMAT)
            type_docteur = fonctions.Cpraticien().encode(FORMAT)
            type_rdv = fonctions.CRdV().encode(FORMAT)
            date_rdv = fonctions.Cjour() + "/" + fonctions.Cmois() + "/" + fonctions.Cannee()
            date_rdv = date_rdv.encode(FORMAT)

            envoi_donnees_prise_rdv = '03pSENDDATARDV'.encode(FORMAT)
            socket.sendall(envoi_donnees_prise_rdv)

            socket.sendall(localisation)
            socket.sendall(type_docteur)
            socket.sendall(type_rdv)
            socket.sendall(date_rdv)
        else:
            raise NotImplementedError

        confirmation_serveur = socket.recv(32)
        confirmation_serveur = confirmation_serveur.decode(FORMAT)

        if confirmation_serveur == '04pINITAFFDISPO':
            str_dico_disponibilites = socket.recv(512).decode(FORMAT)
            dico_disponibilites = fonctions_transfert.from_string_to_dict(str_dico_disponibilites)

            launcher.sequence('IVp',(dico_disponibilites))
            
            if True: #Si le rdv est validé
                envoi_validation_rdv = '04pVALIDATIONRDV'.encode(FORMAT) #Confirmation au serveur qu'on valide le rdv et envoi des infos correspondantes
                nom_docteur_rdv_choisi = fonctions.Ddocname().encode(FORMAT)
                horaire_rdv_choisi = fonctions.DHoraireRdv().encode(FORMAT)
                infos_supp_pour_docteur = fonctions.DInfos().encode(FORMAT)

                socket.sendall(envoi_validation_rdv)
                socket.sendall(nom_docteur_rdv_choisi)
                socket.sendall(horaire_rdv_choisi)
                socket.sendall(infos_supp_pour_docteur)
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

    confirmation_serveur = socket.recv(32).decode(FORMAT)
    if confirmation_serveur == 'VpINITRECAP':
        launcher.sequence('Vp',(date_rdv,horaire_rdv_choisi,nom_docteur_rdv_choisi,'rue à remplir','ville à remplir','code postal à remplir','numéro à remplir','adresse email à remplir',infos_supp_pour_docteur))
    else:
        raise NotImplementedError

    sys.exit()