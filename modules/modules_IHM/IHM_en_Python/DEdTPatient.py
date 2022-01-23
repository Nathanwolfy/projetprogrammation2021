


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Form(object):          
    def __init__(self, arg):
        self.dico = arg                     #Dictionnaire avec pour chaque médecin les rendez-vous disponible pour la journée sélectionnée
        self.continuation = False           #Information envoyée au serveur pour savoir si l'utilisateur a demandé la fermeture de l'application par la croix ou si il a utilisé un bouton permettant de continuer le processus d'utilisation (booléen)
        self.nom_docteur_rdv_choisi = ''    #Information envoyée au serveur par le patient du choix du nom du médecin choisi
        self.horaire_rdv_choisi = ''        #Information envoyée au serveur par le patient du choix de l'horaire du rendez-vous
        self.infos_pour_docteur = ''        #Information envoyée au serveur par le patient sur les informations qu'il souhaite donner au médecin
    

    def setupUi(self, Form):                #Mise en place de l'IHM
        Form.setObjectName("Form")
        Form.resize(720, 615)
        self.Brand_Label = QtWidgets.QLabel(Form)
        self.Brand_Label.setGeometry(QtCore.QRect(280, 10, 171, 71))
        self.Brand_Label.setObjectName("Brand_Label")
        self.listepraticiens_Label = QtWidgets.QLabel(Form)
        self.listepraticiens_Label.setGeometry(QtCore.QRect(0, 120, 301, 41))
        self.listepraticiens_Label.setObjectName("listepraticiens_Label")
        self.ListePraticens_listWidget = QtWidgets.QListWidget(Form)
        self.ListePraticens_listWidget.setGeometry(QtCore.QRect(20, 190, 251, 331))
        self.ListePraticens_listWidget.setObjectName("ListePraticens_listWidget")

        for key in self.dico.keys():                   #Génération de la liste avec le nom des médecins différents disponibles
            self.ListePraticens_listWidget.addItem(key)

        self.Horaire_Label = QtWidgets.QLabel(Form)
        self.Horaire_Label.setGeometry(QtCore.QRect(400, 120, 291, 41))
        self.Horaire_Label.setObjectName("Horaire_Label")
        self.ValidationpushButton = QtWidgets.QPushButton(Form)
        self.ValidationpushButton.setGeometry(QtCore.QRect(310, 550, 111, 41))
        self.ValidationpushButton.setObjectName("ValidationpushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(400, 200, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.Info_Label = QtWidgets.QLabel(Form)
        self.Info_Label.setGeometry(QtCore.QRect(400, 280, 291, 81))
        self.Info_Label.setObjectName("Info_Label")
        self.InfolineEdit = QtWidgets.QLineEdit(Form)
        self.InfolineEdit.setGeometry(QtCore.QRect(410, 380, 251, 31))
        self.InfolineEdit.setObjectName("InfolineEdit")


        self.retranslateUi(Form)

        self.ValidationpushButton.released.connect(lambda: self.set_continuation(True))         #L'utilisateur appuie sur Validation, self.continuation passe en True par la méthode set_continuation()

        self.ValidationpushButton.released.connect(lambda: self.set_horaire_rdv_choisi(self.comboBox.currentText()))        #L'utilisateur appuie sur Validation, self.horaire_rdv_choisi est mise à jour par la méthode set_horaire_rdv_choisi()
        self.ValidationpushButton.released.connect(lambda: self.set_infos_pour_docteur(self.InfolineEdit.text()))           #L'utilisateur appuie sur Validation, self.infos_pour_docteur mise à jour par la méthode set_infos_pour_docteur()
        
        self.ListePraticens_listWidget.currentTextChanged.connect(self.update_rdv_type_combobox)        #L'utilisateur qui sélectionne un médecin dans la liste va mettre à jour les types de rendez-vous dans le menu déroulant                 

        self.ValidationpushButton.released.connect(Form.close)      #L'utilisation du Ferme ferme l'IHM

        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def update_rdv_type_combobox(self, docteur_type):           #Méthode permettant de mettre à jour la rdv_combobox
        self.nom_docteur_rdv_choisi = docteur_type
        self.comboBox.clear()
        if docteur_type in self.dico.keys():
            type_rdv = self.dico[docteur_type]
            for rdv in type_rdv:
                self.comboBox.addItem(rdv)

    def set_continuation(self,valeur):              #Méthode permettant d'associer à self.continuation la valeur que l'on donne en argument
        self.continuation = valeur
    
    def set_horaire_rdv_choisi(self,valeur):        #Méthode permettant d'associer à self.horaire_rdv_choisi la valeur que l'on donne en argument
        self.horaire_rdv_choisi = valeur
    
    def set_infos_pour_docteur(self,valeur):        #Méthode permettant d'associer à self.infos_pour_docteur la valeur que l'on donne en argument
        self.infos_pour_docteur = valeur


    def retranslateUi(self, Form):                  #Mise en forme de l'IHM
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.listepraticiens_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Liste des praticiens disponibles :</span></p></body></html>"))
        __sortingEnabled = self.ListePraticens_listWidget.isSortingEnabled()
        self.ListePraticens_listWidget.setSortingEnabled(False)
        self.ListePraticens_listWidget.setSortingEnabled(__sortingEnabled)
        self.Horaire_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Horaires possibles :</span></p></body></html>"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Info_Label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Informations supplémentaires :</span></p><p align=\"center\"><span style=\" font-size:12pt;\">(Pour le médecin)</span></p></body></html>"))
