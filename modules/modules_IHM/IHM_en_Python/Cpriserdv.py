


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def __init__(self, arg):
        self.dico = arg[0]                  #Le premier élément du tuple envoyé par le serveur à la génération de l'IHM est un dictionnaire rempli d'une liste de type de praticiens en clef avec pour chacune de ces clés le type de rendez-vous que le médecin peut faire
        self.bool = arg[1]                  #Le deuxième élément du tuple envoyé est un booléen qui sera False si le patient a déjà essayé de prendre un rendez-vous mais qu'il n'y en avait pas avec les caractéristiques qu'il a envoyé, l'IHM a été rechargé
        self.continuation = False           #Information envoyée au serveur pour savoir si l'utilisateur a demandé la fermeture de l'application par la croix ou si il a utilisé un bouton permettant de continuer le processus d'utilisation (booléen)
        self.localisation = ''              #Information envoyée au serveur par le patient du choix de la localisation demandée pour le rendez-vous
        self.type_docteur = ''              #Information envoyée au serveur par le patient du choix du type de docteur demandé pour le rendez-vous
        self.type_rdv = ''                  #Information envoyée au serveur par le patient du choix du type de rendez-vous que peut faire le médecin 
        self.jour_rdv = ''                  #Information envoyée au serveur par le patient du choix du jour du rendez-vous
        self.mois_rdv = ''                  #Information envoyée au serveur par le patient du choix du mois du rendez-vous
        self.annee_rdv =''                  #Information envoyée au serveur par le patient du choix du année du rendez-vous


    def setupUi(self, Form):                #Mise en place de l'IHM
        Form.setObjectName("Form")
        Form.resize(545, 439)
        self.Localisation_Label = QtWidgets.QLabel(Form)
        self.Localisation_Label.setGeometry(QtCore.QRect(10, 120, 211, 41))
        self.Localisation_Label.setObjectName("Localisation_Label")
        self.Brand_Label = QtWidgets.QLabel(Form)
        self.Brand_Label.setGeometry(QtCore.QRect(190, 0, 171, 71))
        self.Brand_Label.setObjectName("Brand_Label")
        self.Localisation_LineEdit = QtWidgets.QLineEdit(Form)
        self.Localisation_LineEdit.setGeometry(QtCore.QRect(250, 130, 201, 31))
        self.Localisation_LineEdit.setObjectName("Localisation_LineEdit")
        self.TypePraticien_Label = QtWidgets.QLabel(Form)
        self.TypePraticien_Label.setGeometry(QtCore.QRect(10, 240, 221, 41))
        self.TypePraticien_Label.setObjectName("TypePraticien_Label")
        self.Praticien_comboBox = QtWidgets.QComboBox(Form)
        self.Praticien_comboBox.setGeometry(QtCore.QRect(250, 240, 201, 31))
        self.Praticien_comboBox.setObjectName("Praticien_comboBox")

        for key in self.dico.keys():                        #Génération de la ComboBox Praticien en fonction des types de médecins disponibles sur l'application
            self.Praticien_comboBox.addItem(key)

        self.RdV_Label = QtWidgets.QLabel(Form)
        self.RdV_Label.setGeometry(QtCore.QRect(40, 310, 171, 41))
        self.RdV_Label.setObjectName("RdV_Label")
        self.RdV_comboBox = QtWidgets.QComboBox(Form)
        self.RdV_comboBox.setGeometry(QtCore.QRect(250, 320, 201, 21))
        self.RdV_comboBox.setObjectName("RdV_comboBox")
        self.ValidationpushButton = QtWidgets.QPushButton(Form)
        self.ValidationpushButton.setGeometry(QtCore.QRect(290, 380, 101, 41))
        self.ValidationpushButton.setObjectName("ValidationpushButton")
        self.Date_Label = QtWidgets.QLabel(Form)
        self.Date_Label.setGeometry(QtCore.QRect(10, 180, 241, 41))
        self.Date_Label.setObjectName("Date_Label")
        self.jourLineEdit = QtWidgets.QLineEdit(Form)
        self.jourLineEdit.setGeometry(QtCore.QRect(250, 180, 41, 31))
        self.jourLineEdit.setObjectName("jourLineEdit")
        self.moisLineEdit = QtWidgets.QLineEdit(Form)
        self.moisLineEdit.setGeometry(QtCore.QRect(310, 180, 41, 31))
        self.moisLineEdit.setObjectName("moisLineEdit")
        self.anneeLineEdit = QtWidgets.QLineEdit(Form)
        self.anneeLineEdit.setGeometry(QtCore.QRect(370, 180, 41, 31))
        self.anneeLineEdit.setObjectName("anneeLineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 80, 231, 20))
        self.label.setObjectName("label")
        self.update_rdv_type_combobox(self.Praticien_comboBox.currentText())            #Update de la deuxième ComboBox en fonction de ce qui a été séléctionné avec la première et qui renvoie le type de rendez-vous que peut faire le médecin séléctionné (ex: si c'est un radiologue des radio, si c'est un généraliste une viste annuel ou un certificat)


        self.retranslateUi(Form)

        self.ValidationpushButton.released.connect(lambda: self.set_continuation(True))         #L'utilisateur appuie sur Validation, self.continuation passe en True par la méthode set_continuation()

        self.Praticien_comboBox.currentTextChanged.connect(self.update_rdv_type_combobox)       #L'utilisateur qui sélectionne un médecin dans le menu déroulant va mettre à jour les types de rendez-vous dans le second menu déroulant

        self.ValidationpushButton.released.connect(lambda: self.set_localisation(self.Localisation_LineEdit.text()))        #Le bouton Validation renvoie la localisation rentrée dans la zone de texte LineEdit dans self.localisation au moyen de la fonction set_localisation()         
        self.ValidationpushButton.released.connect(lambda: self.set_type_docteur(self.Praticien_comboBox.currentText()))    #Le bouton Validation renvoie le type de médecin sélectionné dans le menu déroulant dans self.type_docteur au moyen de la fonction set_type_docteur()
        self.ValidationpushButton.released.connect(lambda: self.set_type_rdv(self.RdV_comboBox.currentText()))              #Le bouton Validation renvoie le type de rendez-vous sélectionné dans le menu déroulant dans self.type_rdv au moyen de la fonction set_type_rdv()
        #Le bouton Validation renvoie le jour, le mois et l'année rentrés dans la zone de texte LineEdit dans self.jour_rdv, self.mois_rdv, self.annee_rdv au moyen de la fonction set_date_rdv()
        self.ValidationpushButton.released.connect(lambda: self.set_date_rdv(self.jourLineEdit.text(),self.moisLineEdit.text(),self.anneeLineEdit.text()))

        self.ValidationpushButton.released.connect(Form.close)          #L'utilisation du Validation ferme l'IHM

        QtCore.QMetaObject.connectSlotsByName(Form)


    def set_continuation(self, valeur):             #Méthode permettant d'associer à self.continuation la valeur que l'on donne en argument
        self.continuation = valeur
    
    def set_localisation(self,valeur):              #Méthode permettant d'associer à self.localisation la valeur que l'on donne en argument
        self.localisation = valeur
    
    def set_type_docteur(self,valeur):              #Méthode permettant d'associer à self.type_docteur la valeur que l'on donne en argument
        self.type_docteur = valeur
    
    def set_type_rdv(self,valeur):                  #Méthode permettant d'associer à self.type_rdv la valeur que l'on donne en argument
        self.type_rdv = valeur
    
    def set_date_rdv(self,jour,mois,annee):         #Méthode permettant d'associer à self.jour_rdv, self.mois_rdv et self.annee_rdv la valeur que l'on donne en argument
        self.jour_rdv, self.mois_rdv, self.annee_rdv = jour, mois, annee
    
    def update_rdv_type_combobox(self, docteur_type):       #Méthode permettant de mettre à jour la rdv_combobox
        self.RdV_comboBox.clear()
        if docteur_type in self.dico.keys():
            type_rdv = self.dico[docteur_type]
            for rdv in type_rdv:
                self.RdV_comboBox.addItem(rdv)


    def retranslateUi(self, Form):                  #Mise en forme de l'IHM
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Localisation_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Localisation (Ville) :</span></p></body></html>"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.TypePraticien_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Type de Praticien :</span></p></body></html>"))
        self.RdV_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Type de Rendez-Vous :</span></p></body></html>"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Date_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Date (jj/mm/aaaa) :</span></p></body></html>"))
        if self.bool == False:
            self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Pas de rendez-vous disponible.</span></p></body></html>"))