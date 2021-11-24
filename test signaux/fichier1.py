# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 07:50:48 2021

@author: natha
"""

from PySide6.QtCore import Signal as Signal
from communication import Interface

interface = Interface()

while True:  
    interface.reponse.emit('Hi')
