


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def __init__(self, arg):
        self.arg = arg
        self.continuation = False           #Information envoyée au serveur pour savoir si l'utilisateur a demandé la fermeture de l'application par la croix ou si il a utilisé un bouton permettant de continuer le processus d'utilisation (booléen)
        self.nom_docteur = ''               #Information envoyée au serveur par le docteur de son nom
        self.prenom_docteur = ''            #Information envoyée au serveur par le docteur de son prénom
        self.type_docteur = ''              #Information envoyée au serveur par le docteur de sa spécialité
        self.ville_docteur = ''             #Information envoyée au serveur par le docteur de sa ville de pratique
        self.adresse_docteur = ''           #Information envoyée au serveur par le docteur de son adresse
        self.code_postal_docteur = ''       #Information envoyée au serveur par le docteur de son code postal
        self.numero_docteur = ''            #Information envoyée au serveur par le docteur de son numéro
        self.mail_docteur = ''              #Information envoyée au serveur par le docteur de son mail
        self.mot_de_passe_docteur = ''      #Information envoyée au serveur par le docteur de son mot de passe
        

    def setupUi(self, Form):                #Mise en place de l'IHM
        Form.setObjectName("Form")
        Form.resize(400, 562)
        self.Docteurlabel = QtWidgets.QLabel(Form)
        self.Docteurlabel.setGeometry(QtCore.QRect(150, 40, 91, 51))
        self.Docteurlabel.setObjectName("Docteurlabel")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 151, 51))
        self.label_2.setObjectName("label_2")
        self.NomlineEdit = QtWidgets.QLineEdit(Form)
        self.NomlineEdit.setGeometry(QtCore.QRect(180, 200, 171, 21))
        self.NomlineEdit.setObjectName("NomlineEdit")
        self.Nomlabel = QtWidgets.QLabel(Form)
        self.Nomlabel.setGeometry(QtCore.QRect(30, 200, 121, 21))
        self.Nomlabel.setObjectName("Nomlabel")
        self.Prenomlabel = QtWidgets.QLabel(Form)
        self.Prenomlabel.setGeometry(QtCore.QRect(30, 230, 121, 21))
        self.Prenomlabel.setObjectName("Prenomlabel")
        self.PrenomlineEdit = QtWidgets.QLineEdit(Form)
        self.PrenomlineEdit.setGeometry(QtCore.QRect(180, 230, 171, 21))
        self.PrenomlineEdit.setObjectName("PrenomlineEdit")
        self.Villelabel = QtWidgets.QLabel(Form)
        self.Villelabel.setGeometry(QtCore.QRect(30, 260, 121, 21))
        self.Villelabel.setObjectName("Villelabel")
        self.VillelineEdit = QtWidgets.QLineEdit(Form)
        self.VillelineEdit.setGeometry(QtCore.QRect(180, 260, 171, 21))
        self.VillelineEdit.setObjectName("VillelineEdit")
        self.CodePostallabel = QtWidgets.QLabel(Form)
        self.CodePostallabel.setGeometry(QtCore.QRect(30, 320, 121, 21))
        self.CodePostallabel.setObjectName("CodePostallabel")
        self.CodePostallineEdit = QtWidgets.QLineEdit(Form)
        self.CodePostallineEdit.setGeometry(QtCore.QRect(180, 320, 171, 21))
        self.CodePostallineEdit.setObjectName("CodePostallineEdit")
        self.Adresselabel = QtWidgets.QLabel(Form)
        self.Adresselabel.setGeometry(QtCore.QRect(30, 290, 161, 21))
        self.Adresselabel.setObjectName("Adresselabel")
        self.AdresselineEdit = QtWidgets.QLineEdit(Form)
        self.AdresselineEdit.setGeometry(QtCore.QRect(180, 290, 171, 21))
        self.AdresselineEdit.setObjectName("AdresselineEdit")
        self.Praticien_comboBox = QtWidgets.QComboBox(Form)
        self.Praticien_comboBox.setGeometry(QtCore.QRect(180, 120, 201, 31))
        self.Praticien_comboBox.setObjectName("Praticien_comboBox")
        
        for i in self.arg:                  #Génération du menu déroulant avec les type de spécialitées pour un médecin
            self.Praticien_comboBox.addItem(i)

        self.TypePratiquelabel = QtWidgets.QLabel(Form)
        self.TypePratiquelabel.setGeometry(QtCore.QRect(20, 120, 151, 31))
        self.TypePratiquelabel.setObjectName("TypePratiquelabel")
        self.AdresseMaillabel = QtWidgets.QLabel(Form)
        self.AdresseMaillabel.setGeometry(QtCore.QRect(20, 400, 121, 21))
        self.AdresseMaillabel.setObjectName("AdresseMaillabel")
        self.AdresseMaillineEdit = QtWidgets.QLineEdit(Form)
        self.AdresseMaillineEdit.setGeometry(QtCore.QRect(170, 400, 191, 21))
        self.AdresseMaillineEdit.setObjectName("AdresseMaillineEdit")
        self.ValidationpushButton = QtWidgets.QPushButton(Form)
        self.ValidationpushButton.setGeometry(QtCore.QRect(150, 500, 101, 41))
        self.ValidationpushButton.setObjectName("ValidationpushButton")
        self.Numerolabel = QtWidgets.QLabel(Form)
        self.Numerolabel.setGeometry(QtCore.QRect(30, 350, 161, 21))
        self.Numerolabel.setObjectName("Numerolabel")
        self.NumerolineEdit = QtWidgets.QLineEdit(Form)
        self.NumerolineEdit.setGeometry(QtCore.QRect(180, 350, 171, 21))
        self.NumerolineEdit.setObjectName("NumerolineEdit")
        self.MdPlabel = QtWidgets.QLabel(Form)
        self.MdPlabel.setGeometry(QtCore.QRect(30, 450, 121, 21))
        self.MdPlabel.setObjectName("MdPlabel")
        self.MdPlineEdit = QtWidgets.QLineEdit(Form)
        self.MdPlineEdit.setGeometry(QtCore.QRect(180, 450, 171, 21))
        self.MdPlineEdit.setObjectName("MdPlineEdit")


        self.retranslateUi(Form)

        self.ValidationpushButton.released.connect(lambda: self.set_continuation(True))     #L'utilisateur appuie sur Validation, self.continuation passe en True par la méthode set_continuation()
    
        #Le bouton Validation renvoie le nom du docteur, le prénom, la localisation, le numéro, le mail, le type de docteur et le mot de passe rentrés dans les zones de texte LineEdit au moyen de les méthodes set_nom_docteur(), set_prenom_docteur(), set_localisation_docteur(), set_numero_docteur(), set_mail_docteur(), set_type_docteur() et set_mot_de_passe_docteur()
        self.ValidationpushButton.released.connect(lambda: self.set_nom_docteur(self.NomlineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_prenom_docteur(self.PrenomlineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_localisation_docteur(self.VillelineEdit.text(),self.AdresselineEdit.text(),self.CodePostallineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_numero_docteur(self.NumerolineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_mail_docteur(self.AdresseMaillineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_type_docteur(self.Praticien_comboBox.currentText()))
        self.ValidationpushButton.released.connect(lambda: self.set_mot_de_passe_docteur(self.MdPlineEdit.text()))

        self.ValidationpushButton.released.connect(Form.close)      #L'utilisation du Validation ferme l'IHM

        QtCore.QMetaObject.connectSlotsByName(Form)


    def set_continuation(self,valeur):          #Méthode permettant d'associer à self.continuation la valeur que l'on donne en argument
        self.continuation = valeur
    
    def set_nom_docteur(self,valeur):           #Méthode permettant d'associer à self.nom_docteur la valeur que l'on donne en argument
        self.nom_docteur = valeur
    
    def set_prenom_docteur(self,valeur):        #Méthode permettant d'associer à self.prenom_docteur la valeur que l'on donne en argument
        self.prenom_docteur = valeur
    
    def set_localisation_docteur(self,ville,adresse,code_postal):       #Méthode permettant d'associer à self.ville_docteur, self.adresse_docteur et self.code_postal_docteur la valeur que l'on donne en argument
        self.ville_docteur, self.adresse_docteur, self.code_postal_docteur = ville, adresse, code_postal

    def set_numero_docteur(self,valeur):        #Méthode permettant d'associer à self.numero_docteur la valeur que l'on donne en argument
        self.numero_docteur = valeur
    
    def set_mail_docteur(self,valeur):          #Méthode permettant d'associer à self.mail_docteur la valeur que l'on donne en argument
        self.mail_docteur = valeur
    
    def set_type_docteur(self,valeur):          #Méthode permettant d'associer à self.type_docteur la valeur que l'on donne en argument
        self.type_docteur = valeur
    
    def set_mot_de_passe_docteur(self,valeur):  #Méthode permettant d'associer à self.mot_de_passe_docteur la valeur que l'on donne en argument
        self.mot_de_passe_docteur = valeur


    def retranslateUi(self, Form):              #Mise en forme de l'IHM
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Docteurlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Docteur</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.Nomlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Nom :</span></p></body></html>"))
        self.Prenomlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Prénom :</span></p></body></html>"))
        self.Villelabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Ville de Pratique :</span></p></body></html>"))
        self.CodePostallabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Code Postal :</span></p></body></html>"))
        self.Adresselabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Adresse du cabinet :</span></p></body></html>"))      
        self.TypePratiquelabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Type de Pratique :</span></p></body></html>"))
        self.AdresseMaillabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Adresse Mail :</span></p></body></html>"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Numerolabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Numéro :</span></p></body></html>"))
        self.MdPlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Mot de Passe :</span></p></body></html>"))
