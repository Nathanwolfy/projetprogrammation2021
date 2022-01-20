# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\modules\IHM\IHM_en_Qt\3priserdv.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def __init__(self, arg):
        self.dico = arg[0]
        self.bool = arg[1]
        self.continuation = False
        self.localisation = ''
        self.type_docteur = ''
        self.type_rdv = ''
        self.jour_rdv = ''
        self.mois_rdv = ''
        self.annee_rdv =''

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

        for key in self.dico.keys():
            self.Praticien_comboBox.addItem(key)

        self.RdV_Label = QtWidgets.QLabel(Form)
        self.RdV_Label.setGeometry(QtCore.QRect(40, 310, 171, 41))
        self.RdV_Label.setObjectName("RdV_Label")
        self.RdV_comboBox = QtWidgets.QComboBox(Form)
        self.RdV_comboBox.setGeometry(QtCore.QRect(250, 320, 201, 21))
        self.RdV_comboBox.setObjectName("RdV_comboBox")
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
        self.update_rdv_type_combobox(self.Praticien_comboBox.currentText())

        self.retranslateUi(Form)

        self.ValidationpushButton.released.connect(lambda: self.set_continuation(True))

        self.Localisation_LineEdit.textEdited['QString'].connect(self.Praticien_comboBox.show) # type: ignore
        self.Praticien_comboBox.currentTextChanged.connect(self.update_rdv_type_combobox)

        self.ValidationpushButton.released.connect(lambda: self.set_localisation(self.Localisation_LineEdit.text()))
        self.ValidationpushButton.released.connect(lambda: self.set_type_docteur(self.Praticien_comboBox.currentText()))
        self.ValidationpushButton.released.connect(lambda: self.set_type_rdv(self.RdV_comboBox.currentText()))
        self.ValidationpushButton.released.connect(lambda: self.set_date_rdv(self.jourLineEdit.text(),self.moisLineEdit.text(),self.anneeLineEdit.text()))

        self.ValidationpushButton.released.connect(Form.close) # type: ignore
        self.ValidationpushButton.released.connect(Form.close)

        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def set_continuation(self, valeur):
        self.continuation = valeur
    
    def set_localisation(self,valeur):
        self.localisation = valeur
    
    def set_type_docteur(self,valeur):
        self.type_docteur = valeur
    
    def set_type_rdv(self,valeur):
        self.type_rdv = valeur
    
    def set_date_rdv(self,jour,mois,annee):
        self.jour_rdv,self.mois_rdv,self.annee_rdv = jour,mois,annee
    
    #slot permettant de mettre à jour la rdv_combobox
    def update_rdv_type_combobox(self, docteur_type):
        self.RdV_comboBox.clear()
        if docteur_type in self.dico.keys():
            type_rdv = self.dico[docteur_type]
            for rdv in type_rdv:
                self.RdV_comboBox.addItem(rdv)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Localisation_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Localisation (Ville) :</span></p></body></html>"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctoLibre</span></p></body></html>"))
        self.TypePraticien_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Type de Praticien :</span></p></body></html>"))
        self.RdV_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Type de Rendez-Vous :</span></p></body></html>"))
        self.ValidationpushButton.setText(_translate("Form", "Validation"))
        self.Date_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Date (jj/mm/aaaa) :</span></p></body></html>"))
        if self.bool == False:
            self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Pas de rendez-vous disponible.</span></p></body></html>"))