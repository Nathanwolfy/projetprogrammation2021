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

class Achoixdocuser_herit(Achoixdocuser.Ui_Form):
    def __init__(self):
        super().__init__()

class Bconnexionouinscription_herit(Bconnexionouinscription.Ui_Form):
    def __init__(self,arg):
        super().__init__(arg)

class Cpriserdv_herit(Cpriserdv.Ui_Form):
    def __init__(self,arg):
        super().__init__(arg)

class DEdTPatient_herit(DEdTPatient.Ui_Form):
    def __init__(self,arg):
        super().__init__(arg)

class DEdTDoc_herit(DEdTDoc.Ui_Form):
    def __init__(self,arg):
        super().__init__(arg)

class Erecap_herit(Erecap.Ui_Form):
    def __init__(self,arg):
        super().__init__(arg)

class InscriptionPat_herit(InscriptionPat.Ui_Form):
    def __init__(self):
        super().__init__()
    
class InscriptionDoc_herit(InscriptionDoc.Ui_Form):
    def __init__(self,arg):
        super().__init__(arg)

class InscriptionDocedt_herit(InscriptionDocedt.Ui_Form):
    def __init__(self):
        super().__init__()

appS = QtWidgets.QApplication(sys.argv)

def exec_fenetre(fenetre):
    widget = QtWidgets.QWidget()
    mycustomwidget = fenetre
    mycustomwidget.setupUi(widget)
    widget.show()
    appS.exec()

#Module permettant de lancer les différentes IHM dans lequel on importe tous les modules d'IHM codées en python