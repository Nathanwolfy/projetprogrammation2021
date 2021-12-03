# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 07:51:26 2021

@author: nathanwolfy
"""

from PySide6.QtCore import Signal as Signal
from communication import Interface

def connexion(text):
    print(text)
    

interface = Interface()

interface.reponse.connect(lambda text : text)

while True:
    pass