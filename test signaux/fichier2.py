# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 07:51:26 2021

@author: nathanwolfy
"""

from PySide6.QtCore import Signal as Signal
from communication import Interface

def connexion():
    print ("hi it's me fichier2")
    

interface = Interface()

interface.reponse.connect(connexion)