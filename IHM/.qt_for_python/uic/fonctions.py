#Import ce fichier dans tous les fichiers venant de Qt
#import fonctions

metier = ''
identifiant = ''
motdepass = ''
n = ''

def affiche(texte):
    global metier
    metier = texte

def verificationId(texte):
    global identifiant
    identifiant = texte

def verificationMdP(texte):
    global motdepass
    motdepass = texte


def imprime(texte):
    print(texte)

def connection(commande):
    global n 
    n = commande
    








"""
        self.retranslateUi(Form)
        self.DoctorButton.released.connect(Form.close) # type: ignore
        self.PatientButton.released.connect(Form.close) # type: ignore
        self.PatientButton.released.connect(lambda: fonctions.affiche("Patient"))
        self.DoctorButton.released.connect(lambda: fonctions.affiche("Doctor"))
        self.PatientButton.released.connect(lambda: fonctions.connection("continue"))
        self.DoctorButton.released.connect(lambda: fonctions.connection("continue"))
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.retranslateUi(Form)
        self.ConnexionButton.clicked['QAbstractButton*'].connect(self.NomPrenom_LineEdit.copy) # type: ignore
        self.ConnexionButton.clicked['QAbstractButton*'].connect(lambda: fonctions.verificationId(self.NomPrenom_LineEdit.text()))
        self.ConnexionButton.clicked['QAbstractButton*'].connect(lambda: fonctions.imprime(self.NomPrenom_LineEdit.text()))
        self.ConnexionButton.clicked['QAbstractButton*'].connect(self.Mdp_LineEdit.copy) # type: ignore
        self.ConnexionButton.clicked['QAbstractButton*'].connect(lambda: fonctions.verificationMdP(self.Mdp_LineEdit.text()))
        self.ConnexionButton.clicked['QAbstractButton*'].connect(lambda: fonctions.imprime(self.Mdp_LineEdit.text()))
        self.InscriptionButton.released.connect(Form.close) # type: ignore
        self.InscriptionButton.released.connect(lambda: fonctions.connection("sub"))
        self.B_Retour_commandLinkButton.released.connect(Form.close) # type: ignore
        self.B_Retour_commandLinkButton.released.connect(lambda: fonctions.connection("back"))
        self.NomPrenom_LineEdit.textEdited['QString'].connect(self.Mdp_LineEdit.show) # type: ignore
        self.Mdp_LineEdit.editingFinished.connect(self.ConnexionButton.show) # type: ignore
        self.Mdp_LineEdit.editingFinished.connect(lambda: fonctions.connection("continue"))
        QtCore.QMetaObject.connectSlotsByName(Form)
"""