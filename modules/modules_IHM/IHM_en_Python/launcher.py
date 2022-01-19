from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from . import Achoixdocuser
from . import Bconnexionouinscription
from . import Cpriserdv
from . import DEdTPatient
from . import DEdTDoc
from . import Erecap
from . import InscriptionDoc
from . import InscriptionDocedt
from . import InscriptionPat

seq={'Yp':InscriptionPat, 'YdA':InscriptionDoc, 'YdB': InscriptionDocedt, 'Ig':Achoixdocuser, 'IIg':Bconnexionouinscription, 'IIIp':Cpriserdv, 'IVp' :DEdTPatient, 'IVd' : DEdTDoc, 'Vp': Erecap}

"""
appS = QtWidgets.QApplication(sys.argv)

def sequence(i, arg=[0,0]):
    widget = QtWidgets.QWidget()
    mycustomwidget = seq[i].Ui_Form(arg)
    mycustomwidget.setupUi(widget)
    widget.show()
    appS.exec()"""

class Achoixdocuser_herit(Achoixdocuser.Ui_Form):
    def __init__(self):
        super().__init__()

appS = QtWidgets.QApplication(sys.argv)

def exec_fenetre(fenetre):
    widget = QtWidgets.QWidget()
    mycustomwidget = fenetre
    mycustomwidget.setupUi(widget)
    widget.show()
    appS.exec()