# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\IHM\1_choix_client_doc_user.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):
    def __init__(self,arg):
        self.arg = arg
        self.choix_client = ''
        self.continuation = False
        

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

        self.retranslateUi(Form)

        self.DoctorButton.released.connect(lambda: self.add(self.continuation, True))
        self.PatientButton.released.connect(lambda: self.add(self.continuation, True))  

        self.DoctorButton.released.connect(lambda: self.add(self.choix_client, 'XXd'))
        self.PatientButton.released.connect(lambda: self.add(self.choix_client, 'XXp'))  

        self.DoctorButton.released.connect(Form.close) # type: ignore
        self.PatientButton.released.connect(Form.close) # type: ignore

        QtCore.QMetaObject.connectSlotsByName(Form)

    def add(self, var, arg):
        var = arg

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.DoctorButton.setText(_translate("Form", "Docteur"))
        self.PatientButton.setText(_translate("Form", "Patient"))

