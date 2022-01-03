from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import Achoixdocuser
import Bconnexionouinscription
import Cpriserdv
import DEdTPraticiens
import fonctions

a = Achoixdocuser
b = Bconnexionouinscription
c = Cpriserdv
d = DEdTPraticiens
f = fonctions

seq={1:a, 2:b, 2:c, 3:c, 4:d}

def sequence(i):
    appS = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    mycustomwidget = seq[i].Ui_Form()
    mycustomwidget.setupUi(widget)
    widget.show()
    appS.exec()       
    