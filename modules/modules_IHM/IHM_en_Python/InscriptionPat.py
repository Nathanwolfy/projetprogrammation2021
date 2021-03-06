


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def __init__(self):
        self.continuation = False           #Information envoyée au serveur pour savoir si l'utilisateur a demandé la fermeture de l'application par la croix ou si il a utilisé un bouton permettant de continuer le processus d'utilisation (booléen)
        self.nom_patient = ''               #Information envoyée au serveur par le patient de son nom
        self.prenom_patient = ''            #Information envoyée au serveur par le patient de son prénom
        self.jour_patient = ''              #Information envoyée au serveur par le patient de son jour de naissance
        self.mois_patient = ''              #Information envoyée au serveur par le patient de son mois de naissance
        self.annee_patient = ''             #Information envoyée au serveur par le patient de son année de naissance
        self.mail_patient = ''              #Information envoyée au serveur par le patient de son adresse mail
        self.numero_patient = ''            #Information envoyée au serveur par le patient de son numéro
        self.motdepasse_patient = ''        #Information envoyée au serveur par le patient de son mot de passe



    def setupUi(self, Form):                #Mise en place de l'IHM
        Form.setObjectName("Form")
        Form.resize(400, 424)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 151, 51))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 40, 91, 51))
        self.label.setObjectName("label")
        self.Nomlabel = QtWidgets.QLabel(Form)
        self.Nomlabel.setGeometry(QtCore.QRect(20, 130, 121, 21))
        self.Nomlabel.setObjectName("Nomlabel")
        self.NomlineEdit = QtWidgets.QLineEdit(Form)
        self.NomlineEdit.setGeometry(QtCore.QRect(190, 130, 181, 21))
        self.NomlineEdit.setObjectName("NomlineEdit")
        self.PrenomlineEdit = QtWidgets.QLineEdit(Form)
        self.PrenomlineEdit.setGeometry(QtCore.QRect(190, 160, 181, 21))
        self.PrenomlineEdit.setObjectName("PrenomlineEdit")
        self.Prenomlabel = QtWidgets.QLabel(Form)
        self.Prenomlabel.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.Prenomlabel.setObjectName("Prenomlabel")
        self.DateNaissancelabel = QtWidgets.QLabel(Form)
        self.DateNaissancelabel.setGeometry(QtCore.QRect(20, 190, 161, 21))
        self.DateNaissancelabel.setObjectName("DateNaissancelabel")
        self.jourlineEdit = QtWidgets.QLineEdit(Form)
        self.jourlineEdit.setGeometry(QtCore.QRect(190, 190, 21, 21))
        self.jourlineEdit.setText("")
        self.jourlineEdit.setObjectName("jourlineEdit")
        self.AdresseMaillabel = QtWidgets.QLabel(Form)
        self.AdresseMaillabel.setGeometry(QtCore.QRect(20, 270, 121, 21))
        self.AdresseMaillabel.setObjectName("AdresseMaillabel")
        self.AdresseMaillineEdit = QtWidgets.QLineEdit(Form)
        self.AdresseMaillineEdit.setGeometry(QtCore.QRect(190, 270, 181, 21))
        self.AdresseMaillineEdit.setObjectName("AdresseMaillineEdit")
        self.ValidationpushButton = QtWidgets.QPushButton(Form)
        self.ValidationpushButton.setGeometry(QtCore.QRect(150, 370, 101, 41))
        self.ValidationpushButton.setObjectName("ValidationpushButton")
        self.Numerolabel = QtWidgets.QLabel(Form)
        self.Numerolabel.setGeometry(QtCore.QRect(20, 220, 161, 21))
        self.Numerolabel.setObjectName("Numerolabel")
        self.NumerolineEdit = QtWidgets.QLineEdit(Form)
        self.NumerolineEdit.setGeometry(QtCore.QRect(190, 220, 181, 21))
        self.NumerolineEdit.setObjectName("NumerolineEdit")
        self.MdPlineEdit = QtWidgets.QLineEdit(Form)
        self.MdPlineEdit.setGeometry(QtCore.QRect(190, 320, 181, 21))
        self.MdPlineEdit.setObjectName("MdPlineEdit")
        self.MdPlabel = QtWidgets.QLabel(Form)
        self.MdPlabel.setGeometry(QtCore.QRect(20, 320, 121, 21))
        self.MdPlabel.setObjectName("MdPlabel")
        self.moislineEdit = QtWidgets.QLineEdit(Form)
        self.moislineEdit.setGeometry(QtCore.QRect(220, 190, 21, 21))
        self.moislineEdit.setObjectName("moislineEdit")
        self.anneelineEdit = QtWidgets.QLineEdit(Form)
        self.anneelineEdit.setGeometry(QtCore.QRect(250, 190, 31, 21))
        self.anneelineEdit.setObjectName("anneelineEdit")
        self.jjmmaaaalabel = QtWidgets.QLabel(Form)
        self.jjmmaaaalabel.setGeometry(QtCore.QRect(290, 190, 91, 21))
        self.jjmmaaaalabel.setObjectName("jjmmaaaalabel")
        

        self.retranslateUi(Form)

        self.ValidationpushButton.released.connect(lambda: self.set_continuation(True))     #L'utilisateur appuie sur Validation, self.continuation passe en True par la méthode set_continuation()    

        #Le bouton Validation renvoie le nom du patient, le prénom,la date naissance, le numéro, le mail et le mot de passe rentrés dans les zones de texte LineEdit au moyen de les méthodes set_nom_patient(), set_prenom_patient(), set_numero_patient(), set_mail_patient(), set_numero() et set_mot_de_passe_docteur()
        self.ValidationpushButton.released.connect(lambda: self.set_nom_patient(self.NomlineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_prenom_patient(self.PrenomlineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_date_patient(self.jourlineEdit.text(),self.moislineEdit.text(),self.anneelineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_numero_patient(self.NumerolineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_mail_patient(self.AdresseMaillineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_motdepasse_patient(self.MdPlineEdit.text()))

        self.ValidationpushButton.released.connect(Form.close)          #L'utilisation du Validation ferme l'IHM

        QtCore.QMetaObject.connectSlotsByName(Form)


    def set_continuation(self,valeur):          #Méthode permettant d'associer à self.continuation la valeur que l'on donne en argument
        self.continuation = valeur
    
    def set_nom_patient(self,valeur):           #Méthode permettant d'associer à self.nom_patient la valeur que l'on donne en argument
        self.nom_patient = valeur

    def set_prenom_patient(self,valeur):        #Méthode permettant d'associer à self.prenom_patient la valeur que l'on donne en argument
        self.prenom_patient = valeur
    
    def set_date_patient(self,jour,mois,annee): #Méthode permettant d'associer à self.jour_patient, self.mois_patient et self.annee_patient la valeur que l'on donne en argument
        self.jour_patient, self.mois_patient, self.annee_patient = jour, mois, annee

    def set_numero_patient(self,valeur):        #Méthode permettant d'associer à self.numero_patient la valeur que l'on donne en argument
        self.numero_patient = valeur
    
    def set_mail_patient(self,valeur):          #Méthode permettant d'associer à self.mail_patient la valeur que l'on donne en argument
        self.mail_patient = valeur
    
    def set_motdepasse_patient(self,valeur):    #Méthode permettant d'associer à self.motdepasse_patient la valeur que l'on donne en argument
        self.motdepasse_patient = valeur


    def retranslateUi(self, Form):              #Mise en forme de l'IHM
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Patient</span></p></body></html>"))
        self.Nomlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Nom :</span></p></body></html>"))
        self.Prenomlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Prénom :</span></p></body></html>"))
        self.DateNaissancelabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Date de naissance :</span></p></body></html>"))
        self.AdresseMaillabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Adresse Mail :</span></p></body></html>"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Numerolabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Numéro :</span></p></body></html>"))
        self.MdPlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Mot de Passe :</span></p></body></html>"))
        self.jjmmaaaalabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">jj/mm/aaaa</span></p><p><span style=\" font-size:9pt;\"><br/></span></p></body></html>"))

