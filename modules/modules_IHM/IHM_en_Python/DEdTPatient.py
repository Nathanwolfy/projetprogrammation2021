# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\modules\IHM\IHM_en_Qt\4EdTPatient.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from . import fonctions

class Ui_Form(object):
    def __init__(self, arg):
        self.dico = arg
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 615)
        self.Brand_Label = QtWidgets.QLabel(Form)
        self.Brand_Label.setGeometry(QtCore.QRect(280, 10, 171, 71))
        self.Brand_Label.setObjectName("Brand_Label")
        self.listepraticiens_Label = QtWidgets.QLabel(Form)
        self.listepraticiens_Label.setGeometry(QtCore.QRect(0, 120, 301, 41))
        self.listepraticiens_Label.setObjectName("listepraticiens_Label")
        self.ListePraticens_listWidget = QtWidgets.QListWidget(Form)
        self.ListePraticens_listWidget.setGeometry(QtCore.QRect(20, 190, 251, 331))
        self.ListePraticens_listWidget.setObjectName("ListePraticens_listWidget")

        for key in self.dico.keys():
            self.ListePraticens_listWidget.addItem(key)

        self.Horaire_Label = QtWidgets.QLabel(Form)
        self.Horaire_Label.setGeometry(QtCore.QRect(400, 120, 291, 41))
        self.Horaire_Label.setObjectName("Horaire_Label")
        self.ValidationpushButton = QtWidgets.QPushButton(Form)
        self.ValidationpushButton.setGeometry(QtCore.QRect(310, 550, 111, 41))
        self.ValidationpushButton.setObjectName("ValidationpushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(400, 200, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.Info_Label = QtWidgets.QLabel(Form)
        self.Info_Label.setGeometry(QtCore.QRect(400, 280, 291, 81))
        self.Info_Label.setObjectName("Info_Label")
        self.InfolineEdit = QtWidgets.QLineEdit(Form)
        self.InfolineEdit.setGeometry(QtCore.QRect(410, 380, 251, 31))
        self.InfolineEdit.setObjectName("InfolineEdit")

        self.retranslateUi(Form)

        fonctions.continu(False)
        self.ValidationpushButton.released.connect(lambda: fonctions.continu(True))

        self.ValidationpushButton.released.connect(Form.close) # type: ignore
        self.ValidationpushButton.clicked['bool'].connect(lambda: fonctions.horaire(self.comboBox.currentText()))
        self.ValidationpushButton.clicked['bool'].connect(lambda: fonctions.infodoc(self.InfolineEdit.text()))
        self.ListePraticens_listWidget.currentTextChanged.connect(self.update_rdv_type_combobox)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def update_rdv_type_combobox(self, docteur_type):
        fonctions.medecin(docteur_type)
        self.comboBox.clear()
        if docteur_type in self.dico.keys():
            type_rdv = self.dico[docteur_type]
            for rdv in type_rdv:
                self.comboBox.addItem(rdv)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.listepraticiens_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Liste des praticiens disponibles :</span></p></body></html>"))
        __sortingEnabled = self.ListePraticens_listWidget.isSortingEnabled()
        self.ListePraticens_listWidget.setSortingEnabled(False)
        self.ListePraticens_listWidget.setSortingEnabled(__sortingEnabled)
        self.Horaire_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Horaires possibles :</span></p></body></html>"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Info_Label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Informations supplémentaires :</span></p><p align=\"center\"><span style=\" font-size:12pt;\">(Pour le médecin)</span></p></body></html>"))