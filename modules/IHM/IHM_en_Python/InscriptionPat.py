# Form implementation generated from reading ui file 'c:\Users\Dartencet\Desktop\Sauvgarde ProjetInfo\Autre possibilitée\InscriptionPat.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self,arg):
        self.arg = arg
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 424)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 151, 51))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 40, 91, 51))
        self.label.setObjectName("label")
        self.Nomlabel = QtWidgets.QLabel(Form)
        self.Nomlabel.setGeometry(QtCore.QRect(40, 130, 121, 21))
        self.Nomlabel.setObjectName("Nomlabel")
        self.NomlineEdit = QtWidgets.QLineEdit(Form)
        self.NomlineEdit.setGeometry(QtCore.QRect(190, 130, 171, 21))
        self.NomlineEdit.setObjectName("NomlineEdit")
        self.PrenomlineEdit = QtWidgets.QLineEdit(Form)
        self.PrenomlineEdit.setGeometry(QtCore.QRect(190, 160, 171, 21))
        self.PrenomlineEdit.setObjectName("PrenomlineEdit")
        self.Prenomlabel = QtWidgets.QLabel(Form)
        self.Prenomlabel.setGeometry(QtCore.QRect(40, 160, 121, 21))
        self.Prenomlabel.setObjectName("Prenomlabel")
        self.DateNaissancelabel = QtWidgets.QLabel(Form)
        self.DateNaissancelabel.setGeometry(QtCore.QRect(40, 190, 161, 21))
        self.DateNaissancelabel.setObjectName("DateNaissancelabel")
        self.DateNaissancelineEdit = QtWidgets.QLineEdit(Form)
        self.DateNaissancelineEdit.setGeometry(QtCore.QRect(190, 190, 171, 21))
        self.DateNaissancelineEdit.setObjectName("DateNaissancelineEdit")
        self.AdresseMaillabel = QtWidgets.QLabel(Form)
        self.AdresseMaillabel.setGeometry(QtCore.QRect(30, 270, 121, 21))
        self.AdresseMaillabel.setObjectName("AdresseMaillabel")
        self.AdresseMaillineEdit = QtWidgets.QLineEdit(Form)
        self.AdresseMaillineEdit.setGeometry(QtCore.QRect(180, 270, 191, 21))
        self.AdresseMaillineEdit.setObjectName("AdresseMaillineEdit")
        self.ValidationpushButton = QtWidgets.QPushButton(Form)
        self.ValidationpushButton.setGeometry(QtCore.QRect(150, 370, 101, 41))
        self.ValidationpushButton.setObjectName("ValidationpushButton")
        self.Numerolabel = QtWidgets.QLabel(Form)
        self.Numerolabel.setGeometry(QtCore.QRect(40, 220, 161, 21))
        self.Numerolabel.setObjectName("Numerolabel")
        self.NumerolineEdit = QtWidgets.QLineEdit(Form)
        self.NumerolineEdit.setGeometry(QtCore.QRect(190, 220, 171, 21))
        self.NumerolineEdit.setObjectName("NumerolineEdit")
        self.MdPlineEdit = QtWidgets.QLineEdit(Form)
        self.MdPlineEdit.setGeometry(QtCore.QRect(190, 320, 171, 21))
        self.MdPlineEdit.setObjectName("MdPlineEdit")
        self.MdPlabel = QtWidgets.QLabel(Form)
        self.MdPlabel.setGeometry(QtCore.QRect(40, 320, 121, 21))
        self.MdPlabel.setObjectName("MdPlabel")

        self.retranslateUi(Form)
        self.ValidationpushButton.released.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctObélix</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Patient</span></p></body></html>"))
        self.Nomlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Nom :</span></p></body></html>"))
        self.Prenomlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Prénom :</span></p></body></html>"))
        self.DateNaissancelabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Date de naissance :</span></p></body></html>"))
        self.AdresseMaillabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Adresse Mail :</span></p></body></html>"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Numerolabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Numéro :</span></p></body></html>"))
        self.MdPlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Mot de Passe :</span></p></body></html>"))
