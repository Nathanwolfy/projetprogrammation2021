from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import Achoixdocuser
import Bconnexionouinscription
import Cpriserdv
import DEdTPraticiens
import InscriptionDoc
import InscriptionPat
import fonctions

Yp = InscriptionPat
Yd = InscriptionDoc
Ig = Achoixdocuser
IIg = Bconnexionouinscription
IIIp = Cpriserdv
IVp = DEdTPraticiens
f = fonctions
#rentrer ca dans le dico

seq={Yp:InscriptionPat, Yd:InscriptionDoc, Ig:Achoixdocuser, IIg:Bconnexionouinscription, IIIp:Cpriserdv, IVp:DEdTPraticiens}

def sequence(i, arg):
    appS = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    mycustomwidget = seq[i].Ui_Form(arg)
    mycustomwidget.setupUi(widget)
    widget.show()
    appS.exec()  

     

