# Form implementation generated from reading ui file 'c:\Users\Dartencet\Documents\GitHub\projetprogrammation2021\modules\IHM\IHM_en_Qt\4EdTDoc.ui'
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
        self.arg = arg

    def setupUi(self, Form):
        n = max((len(self.arg[0]), len(self.arg[1]), len(self.arg[2]), len(self.arg[3]), len(self.arg[4]), len(self.arg[5])))
        Form.setObjectName("Form")
        Form.resize(714, 614)
        self.EdTtableWidget = QtWidgets.QTableWidget(Form)
        self.EdTtableWidget.setGeometry(QtCore.QRect(60, 200, 601, 361))
        self.EdTtableWidget.setObjectName("EdTtableWidget")
        self.EdTtableWidget.setColumnCount(6)
        self.EdTtableWidget.setRowCount(n)
        for i in range(n):
            item = QtWidgets.QTableWidgetItem()
            self.EdTtableWidget.setVerticalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.EdTtableWidget.setHorizontalHeaderItem(5, item)
        for i in range(len(self.arg)):
            for j in range(len(self.arg[i])):
                item = QtWidgets.QTableWidgetItem(self.arg[i][j])
                self.EdTtableWidget.setItem(j, i, item)
                
        self.EdTtableWidget.horizontalHeader().setDefaultSectionSize(96)
        self.EdTtableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.EdTtableWidget.verticalHeader().setDefaultSectionSize(25)
        self.EdTtableWidget.verticalHeader().setMinimumSectionSize(25)
        self.EdT_Label = QtWidgets.QLabel(Form)
        self.EdT_Label.setGeometry(QtCore.QRect(220, 130, 281, 41))
        self.EdT_Label.setObjectName("EdT_Label")
        self.Brand_Label = QtWidgets.QLabel(Form)
        self.Brand_Label.setGeometry(QtCore.QRect(280, 0, 151, 71))
        self.Brand_Label.setObjectName("Brand_Label")
        self.FermepushButton = QtWidgets.QPushButton(Form)
        self.FermepushButton.setGeometry(QtCore.QRect(310, 560, 101, 41))
        self.FermepushButton.setObjectName("FermepushButton")

        self.retranslateUi(Form)

        fonctions.continu(False)
        self.FermepushButton.released.connect(lambda: fonctions.continu(True))

        self.FermepushButton.released.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.EdTtableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Lundi"))
        item = self.EdTtableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mardi"))
        item = self.EdTtableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mercredi"))
        item = self.EdTtableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Jeudi"))
        item = self.EdTtableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Vendredi"))
        item = self.EdTtableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Samedi"))
        __sortingEnabled = self.EdTtableWidget.isSortingEnabled()
        self.EdTtableWidget.setSortingEnabled(False)      
        self.EdTtableWidget.setSortingEnabled(__sortingEnabled)
        self.EdT_Label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Emploi du Temps :</span></p></body></html>"))
        self.Brand_Label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">DoctObélix</span></p></body></html>"))
        self.FermepushButton.setText(_translate("Form", "Fermer"))
        
