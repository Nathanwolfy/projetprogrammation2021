


from PyQt6 import QtCore, QtGui, QtWidgets
import os



class Ui_Form(object):
    def __init__(self, arg):
        self.arg = arg[0]                #Dictionnaire de tous les rendez-vous du médecin qui s'est connecté pour chaque journée. Les clefs sont les jours de la semaine et pour chaque clef les rendez-vous de la journée 
        self.dicojour = [arg[1], arg[2], arg[3], arg[4], arg[5], arg[6]]            #Pour chaque journée un dictionnaire et pour chaque dictionnaire une clef avec un rendez-vous de la journée avec en arguments le nom, le prenom, le motif du rendez-vous et il peut y avoir des informations supplémentaires si le patient en a rentré lors de sa prise de rendez-vous 
        self.continuation = False           #Information envoyée au serveur pour savoir si l'utilisateur a demandé la fermeture de l'application par la croix ou si il a utilisé un bouton permettant de continuer le processus d'utilisation (booléen)

    def setupUi(self, Form):                #Mise en place de l'IHM
        n = max([len(self.dicojour[i]) for i in range(1,len(self.dicojour))])
        Form.setObjectName("Form")
        Form.resize(714, 614)
        self.EdTtableWidget = QtWidgets.QTableWidget(Form)
        self.EdTtableWidget.setGeometry(QtCore.QRect(60, 200, 601, 361))
        self.EdTtableWidget.setObjectName("EdTtableWidget")
        self.EdTtableWidget.setColumnCount(6)
        self.EdTtableWidget.setRowCount(n)
        for i in range(n):
            item = QtWidgets.QTableWidgetItem()
            self.EdTtableWidget.setVerticalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(5, item)
        for (i,jour) in enumerate(self.dicojour):   #Génération de l'emploi du temps
            for (j,horaire) in enumerate(jour):
                item = QtWidgets.QTableWidgetItem(horaire)
                self.EdTtableWidget.setItem(j, i, item)
                
        self.EdTtableWidget.horizontalHeader().setDefaultSectionSize(96)
        self.EdTtableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.EdTtableWidget.verticalHeader().setDefaultSectionSize(25)
        self.EdTtableWidget.verticalHeader().setMinimumSectionSize(25)
        self.EdT_Label = QtWidgets.QLabel(Form)
        self.EdT_Label.setGeometry(QtCore.QRect(220, 130, 281, 41))
        self.EdT_Label.setObjectName("EdT_Label")
        self.Brand_Label = QtWidgets.QLabel(Form)
        self.Brand_Label.setGeometry(QtCore.QRect(280, 0, 151, 71))
        self.Brand_Label.setObjectName("Brand_Label")
        self.FermepushButton = QtWidgets.QPushButton(Form)
        self.FermepushButton.setGeometry(QtCore.QRect(310, 560, 101, 41))
        self.FermepushButton.setObjectName("FermepushButton")


        self.retranslateUi(Form)

        self.FermepushButton.released.connect(lambda: self.set_continuation(True))      #L'utilisateur appuie sur Ferme, self.continuation passe en True par la méthode set_continuation()

        #Lorsque le médecin sélectionne un rendez-vous sur son emploi du temps, la méthode self.fichier est lancée
        self.EdTtableWidget.clicked.connect(lambda: self.fichier(self.EdTtableWidget.selectedItems()[0].text(), self.dicojour[self.EdTtableWidget.selectedIndexes()[0].column()][self.EdTtableWidget.selectedItems()[0].text()]))

        self.FermepushButton.released.connect(Form.close)               #L'utilisation du Ferme ferme l'IHM

        QtCore.QMetaObject.connectSlotsByName(Form)


    def set_continuation(self,valeur):          #Méthode permettant d'associer à self.continuation la valeur que l'on donne en argument
        self.continuation = valeur

    def fichier(self, horaire, liste ):         #Méthode qui ouvre un fichier texte avec des informations sur le patient dont le médecin a sélectionné le rendez-vous sur son emploi du temps interactif
        myFile = open("Informations.txt", "w+")
        myFile.write("Nom-prénom du patient : "+liste[2]+'\n')
        myFile.write("Motif : "+liste[0]+'\n')
        myFile.write("Horaire : "+ horaire+'\n')
        if liste[1] != '' :
            myFile.write("Informations supplémentaires : "+liste[1]+'\n')
        os.startfile("Informations.txt")


    def retranslateUi(self, Form):                  #Mise en forme de l'IHM
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.EdTtableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Lundi"))
        item = self.EdTtableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mardi"))
        item = self.EdTtableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mercredi"))
        item = self.EdTtableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Jeudi"))
        item = self.EdTtableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Vendredi"))
        item = self.EdTtableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Samedi"))
        __sortingEnabled = self.EdTtableWidget.isSortingEnabled()
        self.EdTtableWidget.setSortingEnabled(False)      
        self.EdTtableWidget.setSortingEnabled(__sortingEnabled)
        self.EdT_Label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Emploi du Temps :</span></p></body></html>"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.FermepushButton.setText(_translate("Form", "Fermer"))
        
