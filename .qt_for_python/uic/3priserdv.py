# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\modules\modules_IHM\IHM_en_Qt\3priserdv.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
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
        self.Praticien_comboBox.addItem("")
        self.RdV_Label = QtWidgets.QLabel(Form)
        self.RdV_Label.setGeometry(QtCore.QRect(40, 310, 171, 41))
        self.RdV_Label.setObjectName("RdV_Label")
        self.RdV_comboBox = QtWidgets.QComboBox(Form)
        self.RdV_comboBox.setGeometry(QtCore.QRect(250, 320, 201, 21))
        self.RdV_comboBox.setObjectName("RdV_comboBox")
        self.C_Retour_commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.C_Retour_commandLinkButton.setGeometry(QtCore.QRect(0, 390, 222, 48))
        self.C_Retour_commandLinkButton.setObjectName("C_Retour_commandLinkButton")
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

        self.retranslateUi(Form)
        self.C_Retour_commandLinkButton.released.connect(Form.close) # type: ignore
        self.Localisation_LineEdit.textEdited['QString'].connect(self.Praticien_comboBox.show) # type: ignore
        self.Praticien_comboBox.activated['QString'].connect(self.RdV_comboBox.show) # type: ignore
        self.RdV_comboBox.activated['QString'].connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Localisation_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Localisation (Ville) :</span></p></body></html>"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctObélix</span></p></body></html>"))
        self.TypePraticien_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Type de Praticien :</span></p></body></html>"))
        self.Praticien_comboBox.setItemText(0, _translate("Form", "Addictologue"))
        self.Praticien_comboBox.setItemText(1, _translate("Form", "Allergologue‎ "))
        self.Praticien_comboBox.setItemText(2, _translate("Form", "Cancérologue‎"))
        self.Praticien_comboBox.setItemText(3, _translate("Form", "Cardiologue‎"))
        self.Praticien_comboBox.setItemText(4, _translate("Form", "Dentiste"))
        self.Praticien_comboBox.setItemText(5, _translate("Form", "Dermatologue"))
        self.Praticien_comboBox.setItemText(6, _translate("Form", "Médecin généraliste"))
        self.Praticien_comboBox.setItemText(7, _translate("Form", "Neurologue‎"))
        self.Praticien_comboBox.setItemText(8, _translate("Form", "Ophtalmologue‎"))
        self.Praticien_comboBox.setItemText(9, _translate("Form", "Orthophoniste"))
        self.Praticien_comboBox.setItemText(10, _translate("Form", "Pédiatre‎"))
        self.Praticien_comboBox.setItemText(11, _translate("Form", "Pneumologue‎"))
        self.Praticien_comboBox.setItemText(12, _translate("Form", "Psychiatre‎"))
        self.Praticien_comboBox.setItemText(13, _translate("Form", "Radiologue‎"))
        self.Praticien_comboBox.setItemText(14, _translate("Form", "Rhumatologue‎"))
        self.Praticien_comboBox.setItemText(15, _translate("Form", "Vétérinaire‎"))
        self.RdV_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Type de Rendez-Vous :</span></p></body></html>"))
        self.C_Retour_commandLinkButton.setText(_translate("Form", "Retour"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Date_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Date (jj/mm/aaaa) :</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">TextLabel  </span><span style=\" color:#000000;\">dddddddddd</span></p></body></html>"))
