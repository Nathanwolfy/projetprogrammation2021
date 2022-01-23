


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def __init__(self):
        self.continuation = False           #Information envoyée au serveur pour savoir si l'utilisateur a demandé la fermeture de l'application par la croix ou si il a utilisé un bouton permettant de continuer le processus d'utilisation (booléen)
        self.lundi = []                     #Information envoyée au serveur par le docteur de ses horaires du lundi
        self.mardi = []                     #Information envoyée au serveur par le docteur de ses horaires du mardi
        self.mercredi = []                  #Information envoyée au serveur par le docteur de ses horaires du mercredi
        self.jeudi = []                     #Information envoyée au serveur par le docteur de ses horaires du jeudi
        self.vendredi = []                  #Information envoyée au serveur par le docteur de ses horaires du vendredi
        self.samedi = []                    #Information envoyée au serveur par le docteur de ses horaires du samedi


    def setupUi(self, Form):                #Mise en place de l'IHM
        Form.setObjectName("Form")
        Form.resize(400, 473)
        self.Brand_Label = QtWidgets.QLabel(Form)
        self.Brand_Label.setGeometry(QtCore.QRect(150, 0, 151, 71))
        self.Brand_Label.setObjectName("Brand_Label")
        self.lundilabel = QtWidgets.QLabel(Form)
        self.lundilabel.setGeometry(QtCore.QRect(30, 170, 71, 16))
        self.lundilabel.setObjectName("lundilabel")
        self.mardilabel = QtWidgets.QLabel(Form)
        self.mardilabel.setGeometry(QtCore.QRect(30, 210, 71, 16))
        self.mardilabel.setObjectName("mardilabel")
        self.mercredilabel = QtWidgets.QLabel(Form)
        self.mercredilabel.setGeometry(QtCore.QRect(30, 250, 71, 16))
        self.mercredilabel.setObjectName("mercredilabel")
        self.jeudilabel = QtWidgets.QLabel(Form)
        self.jeudilabel.setGeometry(QtCore.QRect(30, 290, 71, 16))
        self.jeudilabel.setObjectName("jeudilabel")
        self.vendredilabel = QtWidgets.QLabel(Form)
        self.vendredilabel.setGeometry(QtCore.QRect(30, 330, 71, 16))
        self.vendredilabel.setObjectName("vendredilabel")
        self.samedilabel = QtWidgets.QLabel(Form)
        self.samedilabel.setGeometry(QtCore.QRect(30, 370, 71, 16))
        self.samedilabel.setObjectName("samedilabel")
        self.edtlabel = QtWidgets.QLabel(Form)
        self.edtlabel.setGeometry(QtCore.QRect(120, 70, 171, 20))
        self.edtlabel.setObjectName("edtlabel")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 170, 31, 16))
        self.label.setObjectName("label")
        self.deblunlineEdit = QtWidgets.QLineEdit(Form)
        self.deblunlineEdit.setGeometry(QtCore.QRect(170, 170, 41, 22))
        self.deblunlineEdit.setText("")
        self.deblunlineEdit.setObjectName("deblunlineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 170, 31, 16))
        self.label_2.setObjectName("label_2")
        self.finlunlineEdit = QtWidgets.QLineEdit(Form)
        self.finlunlineEdit.setGeometry(QtCore.QRect(280, 170, 41, 22))
        self.finlunlineEdit.setText("")
        self.finlunlineEdit.setObjectName("finlunlineEdit")
        self.debmarlineEdit = QtWidgets.QLineEdit(Form)
        self.debmarlineEdit.setGeometry(QtCore.QRect(170, 210, 41, 22))
        self.debmarlineEdit.setText("")
        self.debmarlineEdit.setObjectName("debmarlineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 210, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(130, 210, 31, 16))
        self.label_4.setObjectName("label_4")
        self.finmarlineEdit = QtWidgets.QLineEdit(Form)
        self.finmarlineEdit.setGeometry(QtCore.QRect(280, 210, 41, 22))
        self.finmarlineEdit.setText("")
        self.finmarlineEdit.setObjectName("finmarlineEdit")
        self.debmerlineEdit = QtWidgets.QLineEdit(Form)
        self.debmerlineEdit.setGeometry(QtCore.QRect(170, 250, 41, 22))
        self.debmerlineEdit.setText("")
        self.debmerlineEdit.setObjectName("debmerlineEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 250, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(130, 250, 31, 16))
        self.label_6.setObjectName("label_6")
        self.finmerlineEdit = QtWidgets.QLineEdit(Form)
        self.finmerlineEdit.setGeometry(QtCore.QRect(280, 250, 41, 22))
        self.finmerlineEdit.setText("")
        self.finmerlineEdit.setObjectName("finmerlineEdit")
        self.deblunlineEdit_4 = QtWidgets.QLineEdit(Form)
        self.deblunlineEdit_4.setGeometry(QtCore.QRect(170, 330, 41, 22))
        self.deblunlineEdit_4.setText("")
        self.deblunlineEdit_4.setObjectName("deblunlineEdit_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(240, 330, 31, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(130, 330, 31, 16))
        self.label_8.setObjectName("label_8")
        self.finlunlineEdit_4 = QtWidgets.QLineEdit(Form)
        self.finlunlineEdit_4.setGeometry(QtCore.QRect(280, 330, 41, 22))
        self.finlunlineEdit_4.setText("")
        self.finlunlineEdit_4.setObjectName("finlunlineEdit_4")
        self.debvenlineEdit = QtWidgets.QLineEdit(Form)
        self.debvenlineEdit.setGeometry(QtCore.QRect(170, 330, 41, 22))
        self.debvenlineEdit.setText("")
        self.debvenlineEdit.setObjectName("debvenlineEdit")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(240, 330, 31, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(130, 330, 31, 16))
        self.label_10.setObjectName("label_10")
        self.finvenlineEdit = QtWidgets.QLineEdit(Form)
        self.finvenlineEdit.setGeometry(QtCore.QRect(280, 330, 41, 22))
        self.finvenlineEdit.setText("")
        self.finvenlineEdit.setObjectName("finvenlineEdit")
        self.debsamlineEdit = QtWidgets.QLineEdit(Form)
        self.debsamlineEdit.setGeometry(QtCore.QRect(170, 370, 41, 22))
        self.debsamlineEdit.setText("")
        self.debsamlineEdit.setObjectName("debsamlineEdit")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(240, 370, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(130, 370, 31, 16))
        self.label_12.setObjectName("label_12")
        self.finsamlineEdit = QtWidgets.QLineEdit(Form)
        self.finsamlineEdit.setGeometry(QtCore.QRect(280, 370, 41, 22))
        self.finsamlineEdit.setText("")
        self.finsamlineEdit.setObjectName("finsamlineEdit")
        self.debjeulineEdit = QtWidgets.QLineEdit(Form)
        self.debjeulineEdit.setGeometry(QtCore.QRect(170, 290, 41, 22))
        self.debjeulineEdit.setText("")
        self.debjeulineEdit.setObjectName("debjeulineEdit")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(240, 290, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(130, 290, 31, 16))
        self.label_14.setObjectName("label_14")
        self.finjeulineEdit = QtWidgets.QLineEdit(Form)
        self.finjeulineEdit.setGeometry(QtCore.QRect(280, 290, 41, 22))
        self.finjeulineEdit.setText("")
        self.finjeulineEdit.setObjectName("finjeulineEdit")
        self.ValidationButton = QtWidgets.QPushButton(Form)
        self.ValidationButton.setGeometry(QtCore.QRect(160, 420, 93, 28))
        self.ValidationButton.setObjectName("ValidationButton")
        self.info2label = QtWidgets.QLabel(Form)
        self.info2label.setGeometry(QtCore.QRect(0, 120, 401, 20))
        self.info2label.setObjectName("info2label")
        self.info1label = QtWidgets.QLabel(Form)
        self.info1label.setGeometry(QtCore.QRect(0, 100, 401, 16))
        self.info1label.setObjectName("info1label")


        self.retranslateUi(Form)

        self.ValidationButton.released.connect(lambda: self.set_continuation(True))         #L'utilisateur appuie sur Validation, self.continuation passe en True par la méthode set_continuation()

        #Le bouton Validation renvoie les horaires pour lundi, mardi, mercredi, jeudi, vendredi, samedi rentrés dans les zones de texte LineEdit dans les listes self.lundi, self,.mardi, self.mercredi, self.jeudi, self.vendredi et self.samedi
        self.ValidationButton.released.connect(lambda: self.lundi.append(self.deblunlineEdit.text(), self.finlunlineEdit.text()))
        self.ValidationButton.released.connect(lambda: self.mardi.append(self.debmarlineEdit.text(), self.finmarlineEdit.text()))
        self.ValidationButton.released.connect(lambda: self.mercredi.append(self.debmerlineEdit.text(), self.finmerlineEdit.text()))
        self.ValidationButton.released.connect(lambda: self.jeudi.append(self.debjeulineEdit.text(), self.finjeulineEdit.text()))
        self.ValidationButton.released.connect(lambda: self.vendredi.append(self.debvenlineEdit.text(), self.finvenlineEdit.text()))
        self.ValidationButton.released.connect(lambda: self.samedi.append(self.debsamlineEdit.text(), self.finsamlineEdit.text()))
  
        self.ValidationButton.released.connect(Form.close)      #L'utilisation du Validation ferme l'IHM

        QtCore.QMetaObject.connectSlotsByName(Form)


    def set_continuation(self,valeur):                  #Méthode permettant d'associer à self.continuation la valeur que l'on donne en argument
        self.continuation = valeur


    def retranslateUi(self, Form):          #Mise en forme de l'IHM
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.lundilabel.setText(_translate("Form", "Lundi :"))
        self.mardilabel.setText(_translate("Form", "Mardi :"))
        self.mercredilabel.setText(_translate("Form", "Mercredi :"))
        self.jeudilabel.setText(_translate("Form", "Jeudi :"))
        self.vendredilabel.setText(_translate("Form", "Vendredi :"))
        self.samedilabel.setText(_translate("Form", "Samedi :"))
        self.edtlabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Emploi du temps :</span></p></body></html>"))
        self.label.setText(_translate("Form", "de "))
        self.label_2.setText(_translate("Form", "à"))
        self.label_3.setText(_translate("Form", "à"))
        self.label_4.setText(_translate("Form", "de "))
        self.label_5.setText(_translate("Form", "à"))
        self.label_6.setText(_translate("Form", "de "))
        self.label_7.setText(_translate("Form", "à"))
        self.label_8.setText(_translate("Form", "de "))
        self.label_9.setText(_translate("Form", "à"))
        self.label_10.setText(_translate("Form", "de "))
        self.label_11.setText(_translate("Form", "à"))
        self.label_12.setText(_translate("Form", "de "))
        self.label_13.setText(_translate("Form", "à"))
        self.label_14.setText(_translate("Form", "de "))
        self.ValidationButton.setText(_translate("Form", "Valider"))
        self.info2label.setText(_translate("Form", "   écrire l\'heure de début et l\'heure de fin de la journée (ex : 8:00 )"))
        self.info1label.setText(_translate("Form", "   Ne rien écrire en cas de non disponibilité une journée, "))
