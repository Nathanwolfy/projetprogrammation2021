from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from . import Achoixdocuser
from . import Bconnexionouinscription
from . import Cpriserdv
from . import DEdTPatient
from . import DEdTDoc
from . import InscriptionDoc
from . import InscriptionPat
from . import Erecap
from . import fonctions

seq={'Yp':InscriptionPat, 'Yd':InscriptionDoc, 'Ig':Achoixdocuser, 'IIg':Bconnexionouinscription, 'IIIp':Cpriserdv, 'IVp' :DEdTPatient, 'IVd' : DEdTDoc, 'Vp': Erecap}

appS = QtWidgets.QApplication(sys.argv)
def sequence(i, arg):
    widget = QtWidgets.QWidget()
    mycustomwidget = seq[i].Ui_Form(arg)
    mycustomwidget.setupUi(widget)
    widget.show()
    appS.exec()