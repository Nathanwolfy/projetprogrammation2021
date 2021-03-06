


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def __init__(self):
        self.choix_client = ''              #Information du choix entre docteur et patient envoyée au serveur
        self.continuation = False           #Information envoyée au serveur pour savoir si l'utilisateur a demandé la fermeture de l'application par la croix ou si il a utilisé un bouton permettant de continuer le processus d'utilisation (booléen)


    def setupUi(self, Form):                #Mise en place de l'IHM
        Form.setObjectName("Form")
        Form.resize(400, 331)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 401, 51))
        self.label.setObjectName("label")
        self.DoctorButton = QtWidgets.QPushButton(Form)
        self.DoctorButton.setGeometry(QtCore.QRect(20, 170, 161, 61))
        self.DoctorButton.setObjectName("DoctorButton")
        self.PatientButton = QtWidgets.QPushButton(Form)
        self.PatientButton.setGeometry(QtCore.QRect(220, 170, 161, 61))
        self.PatientButton.setObjectName("PatientButton")


        self.retranslateUi(Form)

        self.DoctorButton.released.connect(lambda: self.set_continuation(True))     #L'utilisateur appuie sur Docteur, self.continuation passe en True par la Méthode set_continuation()
        self.PatientButton.released.connect(lambda: self.set_continuation(True))    #L'utilisateur appuie sur Patient, self.continuation passe en True par la Méthode set_continuation()
        
        self.DoctorButton.released.connect(lambda: self.set_choix('XXd'))           #Le serveur recoit une chaîne de caractère lui permettant de savoir que le bouton Docteur a été utilisé en modifiant self.choix au moyen de la Méthode set_choix()
        self.PatientButton.released.connect(lambda: self.set_choix('XXp'))          #Le serveur recoit une chaîne de caractère lui permettant de savoir que le bouton Patient a été utilisé en modifiant self.choix au moyen de la Méthode set_choix()

        self.DoctorButton.released.connect(Form.close)                      #L'utilisation du bouton Docteur ferme l'IHM 
        self.PatientButton.released.connect(Form.close)                     #L'utilisation du bouton Patient ferme l'IHM

        QtCore.QMetaObject.connectSlotsByName(Form)


    def set_continuation(self, valeur):                     #Méthode permettant d'associer à self.continuation la valeur que l'on donne en argument
        self.continuation = valeur                          

    def set_choix(self, valeur):                            #Méthode permettant d'associer à self.choix_client la valeur que l'on donne en argument
        self.choix_client = valeur


    def retranslateUi(self, Form):              #Mise en forme de l'IHM
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.DoctorButton.setText(_translate("Form", "Docteur"))
        self.PatientButton.setText(_translate("Form", "Patient"))

