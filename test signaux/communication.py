# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:05:04 2021

@author: natha
"""

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class Interface(QObject):
    
    # Signal pour envoyer une requete
    requete = pyqtSignal(str)
    # Signal pour recevoir une reponse
    reponse = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def emettre_reponse(self,text):
        self.reponse.emit(text)
        

if __name__ == '__main__':
    interface = Interface()
    interface.emettre('hi') 