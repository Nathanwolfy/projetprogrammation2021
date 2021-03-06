


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self,arg):
        self.arg = arg                      #Str envoyée par le serveur lorsque qu'une connexion n'a pas fonctionnée permettant de signaler à l'utilisateur que son identifiant ou son mot de passe à un problème 
        self.continuation = False           #Information envoyée au serveur pour savoir si l'utilisateur a demandé la fermeture de l'application par la croix ou si il a utilisé un bouton permettant de continuer le processus d'utilisation. (booléen)
        self.creation_compte = False        #Information envoyée au serveur sur le choix de l'utilisateur entre Connexion et Inscription. True si il désire créer un compte (booléen)
        self.identifiant_client = ''        #Identifiant du client sous forme de str envoyée au serveur pour vérification
        self.motdepasse_client = ''         #Mot de passe du client sous forme de str envoyée au serveur pour vérification
        

    def setupUi(self, Form):                #Mise en place de l'IHM
        Form.setObjectName("Form")
        Form.resize(720, 570)
        self.labelNomPrenom = QtWidgets.QLabel(Form)
        self.labelNomPrenom.setGeometry(QtCore.QRect(340, 160, 351, 41))
        self.labelNomPrenom.setObjectName("labelNomPrenom")
        self.labelMdP = QtWidgets.QLabel(Form)
        self.labelMdP.setGeometry(QtCore.QRect(340, 310, 351, 41))
        self.labelMdP.setObjectName("labelMdP")
        self.labelConnexion = QtWidgets.QLabel(Form)
        self.labelConnexion.setGeometry(QtCore.QRect(290, 60, 381, 61))
        self.labelConnexion.setObjectName("labelConnexion")
        self.Brand_Label = QtWidgets.QLabel(Form)
        self.Brand_Label.setGeometry(QtCore.QRect(30, 20, 171, 71))
        self.Brand_Label.setObjectName("Brand_Label")
        self.Identifiant_LineEdit = QtWidgets.QLineEdit(Form)
        self.Identifiant_LineEdit.setGeometry(QtCore.QRect(340, 240, 241, 31))
        self.Identifiant_LineEdit.setObjectName("NomPrenom_LineEdit")
        self.Mdp_LineEdit = QtWidgets.QLineEdit(Form)
        self.Mdp_LineEdit.setGeometry(QtCore.QRect(340, 390, 241, 31))
        self.Mdp_LineEdit.setObjectName("Mdp_LineEdit")
        self.InscriptionButton = QtWidgets.QPushButton(Form)
        self.InscriptionButton.setGeometry(QtCore.QRect(70, 344, 161, 28))
        self.InscriptionButton.setObjectName("InscriptionButton")
        self.Inscriptionlabel = QtWidgets.QLabel(Form)
        self.Inscriptionlabel.setGeometry(QtCore.QRect(50, 260, 201, 31))
        self.Inscriptionlabel.setObjectName("Inscriptionlabel")
        self.ConnexionButton = QtWidgets.QPushButton(Form)
        self.ConnexionButton.setGeometry(QtCore.QRect(380, 470, 161, 28))
        self.ConnexionButton.setObjectName("ConnexionButton")


        self.retranslateUi(Form)
        
        self.InscriptionButton.released.connect(lambda: self.set_continuation(True))        #L'utilisateur appuie sur Inscription, self.continuation passe en True par la Méthode set_continuation()
        self.ConnexionButton.released.connect(lambda: self.set_continuation(True))          #L'utilisateur appuie sur Connexion, self.continuation passe en True par la Méthode set_continuation()

        self.ConnexionButton.released.connect(lambda: self.set_identifiant_client(self.Identifiant_LineEdit.text()))        #Le bouton connexion renvoie l'identifiant rentré dans la zone de texte LineEdit au moyen de la Méthode set_identifiant_client()
        self.ConnexionButton.released.connect(lambda: self.set_motdepasse_client(self.Mdp_LineEdit.text()))                 #Le bouton connexion renvoie le mot de passe rentré dans la zone de texte LineEdit au moyen de la Méthode set_motdepasse_client()
        self.InscriptionButton.released.connect(lambda: self.set_creation_compte(True))                                     #Le bouton inscription renvoie le booléen True si il est séléctionné au moyen de la Méthode set_creation_compte()

        if self.arg != '':
            self.Identifiant_LineEdit.insert(self.arg)                                                                      #Si le serveur ouvre cet IHM avec en argument une str non vide, il est créé une zone de texte lui signalant qu'il y a un problème d'identifiant ou de mot de passe

        self.ConnexionButton.released.connect(Form.close)                   #L'utilisation du Connexion ferme l'IHM
        self.InscriptionButton.released.connect(Form.close)                 #L'utilisation du Inscription ferme l'IHM
        
        QtCore.QMetaObject.connectSlotsByName(Form)


    def set_continuation(self, valeur):             #Méthode permettant d'associer à self.continuation la valeur que l'on donne en argument
        self.continuation = valeur

    def set_identifiant_client(self,valeur):        #Méthode permettant d'associer à self.identifiant_client la valeur que l'on donne en argument
        self.identifiant_client = valeur
    
    def set_motdepasse_client(self,valeur):         #Méthode permettant d'associer à self.motdepasse_client la valeur que l'on donne en argument
        self.motdepasse_client = valeur

    def set_creation_compte(self,valeur):           #Méthode permettant d'associer à self.creation_compte la valeur que l'on donne en argument
        self.creation_compte = valeur


    def retranslateUi(self, Form):                  #Mise en forme de l'IHM
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        if self.arg == '':
            self.labelNomPrenom.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Adresse Mail :</span></p></body></html>"))
        else :
            self.labelNomPrenom.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Adresse Mail :</span><span style=\" color:#ff0000;\">(Mauvaise combinaison).</span></p></body></html>"))
        self.labelMdP.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Mot de Passe : </span></p></body></html>"))
        self.labelConnexion.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Connexion</span></p></body></html>"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.InscriptionButton.setText(_translate("Form", "Créer un compte"))
        self.Inscriptionlabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Inscription</span></p></body></html>"))
        self.ConnexionButton.setText(_translate("Form", "Connexion"))
