# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:05:04 2021

@author: natha
"""

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class Interface(QObject):
    
    # Signal pour recevoir une requete
    requete = pyqtSignal(str)
    # Signal pour envoyer une reponse
    reponse = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def emettre(self,text):
        ''' (str) -> None
        Permet d'envoyer une réponse text via le signal self.reponse'''
        self.reponse.emit(text)
        

if __name__ == '__main__':
    interface = Interface()
    interface.reponse.connect(lambda text: print(text))
    interface.emettre('hi')

    #print(help(Interface.emettre))


'''Idées pour faire fonctionner plusieurs scripts à la fois: 
- Difficulté de python sortir du modèle 'un seul fichier' -> réseau XML-RPC ? xmlrpclib
- POSH
- voir du côté des "socket" 
'''