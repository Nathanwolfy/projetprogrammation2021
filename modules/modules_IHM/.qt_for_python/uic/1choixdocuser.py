# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\IHM\IHM en Qt\1choixdocuser.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
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
        self.A_Retour_commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.A_Retour_commandLinkButton.setGeometry(QtCore.QRect(0, 287, 141, 41))
        self.A_Retour_commandLinkButton.setObjectName("A_Retour_commandLinkButton")

        self.retranslateUi(Form)
        self.DoctorButton.released.connect(Form.close) # type: ignore
        self.PatientButton.released.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctObélix</span></p></body></html>"))
        self.DoctorButton.setText(_translate("Form", "Docteur"))
        self.PatientButton.setText(_translate("Form", "Patient"))
        self.A_Retour_commandLinkButton.setText(_translate("Form", "Annuler"))