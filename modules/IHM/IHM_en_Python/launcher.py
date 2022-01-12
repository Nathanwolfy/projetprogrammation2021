from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from . import Achoixdocuser
from . import Bconnexionouinscription
from . import Cpriserdv
from . import DEdTPraticiens
from . import InscriptionDoc
from . import InscriptionPat
from . import fonctions

seq={'Yp':InscriptionPat, 'Yd':InscriptionDoc, 'Ig':Achoixdocuser, 'IIg':Bconnexionouinscription, 'IIIp':Cpriserdv, 'IVp' :DEdTPraticiens}

def sequence(i, arg):
    appS = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    mycustomwidget = seq[i].Ui_Form()
    mycustomwidget.setupUi(widget)
    widget.show()
    appS.exec()  

     

