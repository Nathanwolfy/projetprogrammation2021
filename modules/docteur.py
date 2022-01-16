import sys

from .IHM.IHM_en_Python import launcher, fonctions
from . import fonctions_transfert, echanges_donnees

FORMAT = 'utf-8'

def client_docteur(socket):
    clef_valide = 'False' #On suppose que la clef est fausse de base pour relancer le widget si elle ne l'est pas
    identifiant = '' #Il n'y a pas d'identifiant saisi au départ
    while clef_valide == 'False':
        confirmation_serveur = echanges_donnees.reception(socket)
        
        if confirmation_serveur == '02dINITCONN':
            launcher.sequence('IIg',identifiant)
            creationcompte_patient = fonctions.Bcreationcompte()
                        
            if not creationcompte_patient: #Le client choisit de rentrer son identifiant et mot de passe
                identifiant = fonctions.Bidentifiant()
                motdepasse = fonctions.Bmotdepass()
                clef_patient = identifiant + " " + motdepasse #On récupère identifiants et mot de passe rentrés par le client
                clef_patient = clef_patient

                envoi_clef_connexion = '02dSENDCLEF'
                echanges_donnees.envoi(socket,envoi_clef_connexion)
                echanges_donnees.envoi(socket,clef_patient)

                clef_valide = echanges_donnees.reception(socket)

            else: #Le client choisit de créer un compte
                launcher.sequence('Yd',[0,0])
                envoi_donnees_inscription_debut = 'YYdINITSENDDATA'
                
                nom_docteur = ''
                prenom_docteur = ''
                ville_de_pratique = ''
                adresse_docteur = ''
                code_postal_docteur = ''
                numero_docteur = ''
                identifiant = ''
                motdepasse = ''
                envoi_donnees_inscription_fin = 'YYdTERMSENDDATA'

                echanges_donnees.envoi(socket,envoi_donnees_inscription_debut)
                echanges_donnees.envoi(socket,nom_docteur)
                echanges_donnees.envoi(socket,prenom_docteur)
                echanges_donnees.envoi(socket,ville_de_pratique)
                echanges_donnees.envoi(socket,adresse_docteur)
                echanges_donnees.envoi(socket,code_postal_docteur)
                echanges_donnees.envoi(socket,numero_docteur)
                echanges_donnees.envoi(socket,identifiant)
                echanges_donnees.envoi(socket,motdepasse)
                echanges_donnees.envoi(socket,envoi_donnees_inscription_fin)
                clef_valide = 'True' #Le docteur a créé son compte, il est donc bien identifié
                
        else:
            raise NotImplementedError