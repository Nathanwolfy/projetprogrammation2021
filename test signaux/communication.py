# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:05:04 2021

@author: natha
"""

from PyQt5.QtCore import pyqtSignal

class Interface:
    
    def __init__(self):
        self.requete = pyqtSignal(str)
        self.reponse = pyqtSignal(str)
        
    def emettre(self,text):
        self.reponse.emit(text)
        

if __name__ == '__main__':
    interface = Interface()
    interface.emettre('hi')