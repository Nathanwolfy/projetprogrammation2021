# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\IHM\InscriptionDoc.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
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
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
        self.Praticien_comboBox.addItem("")
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
        self.ValidationpushButton.released.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Docteurlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Docteur</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctObélix</span></p></body></html>"))
        self.Nomlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Nom :</span></p></body></html>"))
        self.Prenomlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Prénom :</span></p></body></html>"))
        self.Villelabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Ville de Pratique :</span></p></body></html>"))
        self.CodePostallabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Code Postal :</span></p></body></html>"))
        self.Adresselabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Adresse du cabine :</span></p></body></html>"))
        self.Praticien_comboBox.setItemText(0, _translate("Form", "Addictologue"))
        self.Praticien_comboBox.setItemText(1, _translate("Form", "Allergologue‎ "))
        self.Praticien_comboBox.setItemText(2, _translate("Form", "Cancérologue‎"))
        self.Praticien_comboBox.setItemText(3, _translate("Form", "Cardiologue‎"))
        self.Praticien_comboBox.setItemText(4, _translate("Form", "Dentiste"))
        self.Praticien_comboBox.setItemText(5, _translate("Form", "Dermatologue"))
        self.Praticien_comboBox.setItemText(6, _translate("Form", "Médecin généraliste"))
        self.Praticien_comboBox.setItemText(7, _translate("Form", "Neurologue‎"))
        self.Praticien_comboBox.setItemText(8, _translate("Form", "Ophtalmologue‎"))
        self.Praticien_comboBox.setItemText(9, _translate("Form", "Pédiatre‎"))
        self.Praticien_comboBox.setItemText(10, _translate("Form", "Pneumologue‎"))
        self.Praticien_comboBox.setItemText(11, _translate("Form", "Psychiatre‎"))
        self.Praticien_comboBox.setItemText(12, _translate("Form", "Radiologue‎"))
        self.Praticien_comboBox.setItemText(13, _translate("Form", "Rhumatologue‎"))
        self.Praticien_comboBox.setItemText(14, _translate("Form", "Vétérinaire‎"))
        self.TypePratiquelabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Type de Pratique :</span></p></body></html>"))
        self.AdresseMaillabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Adresse Mail :</span></p></body></html>"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Numerolabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Numéro :</span></p></body></html>"))
        self.MdPlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Mot de Passe :</span></p></body></html>"))
