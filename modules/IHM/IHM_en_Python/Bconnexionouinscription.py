# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\IHM\2_connexion_ou_inscription.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
<<<<<<< HEAD
import sys
import fonctions
=======
from . import fonctions
>>>>>>> 77772c89152399340620379e502cbe7bcc02344d


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 570)
        self.ConnexionButton = QtWidgets.QDialogButtonBox(Form)
        self.ConnexionButton.setGeometry(QtCore.QRect(390, 480, 193, 28))
        self.ConnexionButton.setMouseTracking(True)
        self.ConnexionButton.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.ConnexionButton.setObjectName("ConnexionButton")
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
        self.NomPrenom_LineEdit = QtWidgets.QLineEdit(Form)
        self.NomPrenom_LineEdit.setGeometry(QtCore.QRect(340, 240, 241, 31))
        self.NomPrenom_LineEdit.setObjectName("NomPrenom_LineEdit")
        self.Mdp_LineEdit = QtWidgets.QLineEdit(Form)
        self.Mdp_LineEdit.setGeometry(QtCore.QRect(340, 390, 241, 31))
        self.Mdp_LineEdit.setObjectName("Mdp_LineEdit")
        self.InscriptionButton = QtWidgets.QPushButton(Form)
        self.InscriptionButton.setGeometry(QtCore.QRect(70, 344, 161, 28))
        self.InscriptionButton.setObjectName("InscriptionButton")
        self.B_Retour_commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.B_Retour_commandLinkButton.setGeometry(QtCore.QRect(0, 520, 222, 48))
        self.B_Retour_commandLinkButton.setObjectName("B_Retour_commandLinkButton")
        self.Inscriptionlabel = QtWidgets.QLabel(Form)
        self.Inscriptionlabel.setGeometry(QtCore.QRect(50, 260, 201, 31))
        self.Inscriptionlabel.setObjectName("Inscriptionlabel")

        self.retranslateUi(Form)
        self.ConnexionButton.clicked['QAbstractButton*'].connect(self.NomPrenom_LineEdit.copy) # type: ignore
        self.ConnexionButton.clicked['QAbstractButton*'].connect(lambda: fonctions.verificationId(self.NomPrenom_LineEdit.text()))
        self.ConnexionButton.clicked['QAbstractButton*'].connect(lambda: fonctions.imprime(self.NomPrenom_LineEdit.text()))
        self.ConnexionButton.clicked['QAbstractButton*'].connect(self.Mdp_LineEdit.copy) # type: ignore
        self.ConnexionButton.clicked['QAbstractButton*'].connect(lambda: fonctions.verificationMdP(self.Mdp_LineEdit.text()))
        self.ConnexionButton.clicked['QAbstractButton*'].connect(lambda: fonctions.imprime(self.Mdp_LineEdit.text()))
        self.InscriptionButton.released.connect(Form.close) # type: ignore
        self.InscriptionButton.released.connect(lambda: fonctions.connection("sub"))
        self.B_Retour_commandLinkButton.released.connect(Form.close) # type: ignore
        self.B_Retour_commandLinkButton.released.connect(lambda: fonctions.connection("back"))
        self.NomPrenom_LineEdit.textEdited['QString'].connect(self.Mdp_LineEdit.show) # type: ignore
        self.Mdp_LineEdit.editingFinished.connect(self.ConnexionButton.show) # type: ignore
        self.Mdp_LineEdit.editingFinished.connect(lambda: fonctions.connection("continue"))
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelNomPrenom.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Nom et Prénom :</span></p></body></html>"))
        self.labelMdP.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Mot de Passe : </span></p></body></html>"))
        self.labelConnexion.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Connexion</span></p></body></html>"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctObélix</span></p></body></html>"))
        self.InscriptionButton.setText(_translate("Form", "Créer un compte"))
        self.B_Retour_commandLinkButton.setText(_translate("Form", "Retour"))
        self.Inscriptionlabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Inscription</span></p></body></html>"))
