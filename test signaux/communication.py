# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:05:04 2021

@author: natha
"""

from PySide6.QtCore import Signal

class Interface:
    
    def __init__(self):
        self.requete = Signal(str)
        self.reponse = Signal(str)
        
    def emettre(self,text):
        self.reponse.emit(text)
        

if __name__ == '__main__':
    interface = Interface()
    interface.emettre('hi')