# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\modules\modules_IHM\IHM_en_Qt\recapdoc.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):

    def __init__(self, horaire, arg):
        self.horaire = horaire
        self.nom = arg[0]
        self.prenom = arg[1]
        self.motif = arg[2]
        self.info = arg[3]

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 382)
        self.Brand_Label = QtWidgets.QLabel(Form)
        self.Brand_Label.setGeometry(QtCore.QRect(130, 0, 151, 61))
        self.Brand_Label.setObjectName("Brand_Label")
        self.nomlabel = QtWidgets.QLabel(Form)
        self.nomlabel.setGeometry(QtCore.QRect(20, 100, 71, 16))
        self.nomlabel.setObjectName("nomlabel")
        self.prenomlabel = QtWidgets.QLabel(Form)
        self.prenomlabel.setGeometry(QtCore.QRect(20, 150, 71, 16))
        self.prenomlabel.setObjectName("prenomlabel")
        self.motiflabel = QtWidgets.QLabel(Form)
        self.motiflabel.setGeometry(QtCore.QRect(20, 250, 141, 16))
        self.motiflabel.setObjectName("motiflabel")
        self.horairelabel = QtWidgets.QLabel(Form)
        self.horairelabel.setGeometry(QtCore.QRect(20, 200, 55, 16))
        self.horairelabel.setObjectName("horairelabel")
        self.nommodiflabel = QtWidgets.QLabel(Form)
        self.nommodiflabel.setGeometry(QtCore.QRect(110, 100, 281, 16))
        self.nommodiflabel.setObjectName("nommodiflabel")
        self.prenommodiflabel = QtWidgets.QLabel(Form)
        self.prenommodiflabel.setGeometry(QtCore.QRect(110, 150, 281, 16))
        self.prenommodiflabel.setObjectName("prenommodiflabel")
        self.horairemodiflabel = QtWidgets.QLabel(Form)
        self.horairemodiflabel.setGeometry(QtCore.QRect(110, 200, 281, 16))
        self.horairemodiflabel.setObjectName("horairemodiflabel")
        self.motifmodiflabel = QtWidgets.QLabel(Form)
        self.motifmodiflabel.setGeometry(QtCore.QRect(70, 280, 321, 16))
        self.motifmodiflabel.setObjectName("motifmodiflabel")
        if self.info != '':
            self.infosuplabel = QtWidgets.QLabel(Form)
            self.infosuplabel.setGeometry(QtCore.QRect(20, 320, 191, 16))
            self.infosuplabel.setObjectName("infosuplabel")
            self.infomodiflabel = QtWidgets.QLabel(Form)
            self.infomodiflabel.setGeometry(QtCore.QRect(20, 350, 371, 16))
            self.infomodiflabel.setObjectName("infomodiflabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.nomlabel.setText(_translate("Form", "Nom :"))
        self.prenomlabel.setText(_translate("Form", "Prénom :"))
        self.motiflabel.setText(_translate("Form", "Motif du rendez-vous :"))
        self.horairelabel.setText(_translate("Form", "Horaire :"))
        self.nommodiflabel.setText(_translate("Form", "TextLabel"))
        self.prenommodiflabel.setText(_translate("Form", "TextLabel"))
        self.horairemodiflabel.setText(_translate("Form", "TextLabel"))
        self.motifmodiflabel.setText(_translate("Form", "TextLabel"))
        if self.info != '':
            self.infomodiflabel.setText(_translate("Form", self.info))
            self.infosuplabel.setText(_translate("Form", "Informations supplémentaires :"))