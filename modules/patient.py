import time
FORMAT = 'utf-8'
WAITINGTIME = 0.05

def client_patient(socket):

    confirmation_serveur = socket.recv(32)
    confirmation_serveur.decode(FORMAT)

    if confirmation_serveur == '02pINITCONN':
        print("Lancement de l'interface de connexion patient ...")
        pass #TODO Lancement interface QT
        #TODO Proposer la création d'un identifiant de connexion
        identifiant_patient = 'nom.prenom@gmail.com' #Données à récupérer à l'aide de l'interface Qt
        motdepasse_patient = 'motdepasse' #Comment encrypter les mots de passe ?

        identifiant_patient = identifiant_patient.encode(FORMAT)
        motdepasse_patient = motdepasse_patient.encode(FORMAT)

        #On signale au serveur que l'on va envoyer les clés de connexion
        envoi_cles_connexion = '02pSENDCONN'.encode(FORMAT)
        socket.sendall(envoi_cles_connexion)
        time.sleep(WAITINGTIME)
        socket.sendall(identifiant_patient)



    else:
        raise NotImplementedError