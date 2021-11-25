# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 07:36:47 2021

@author: natha
"""
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

def horaire():
    tranche_horaire = [] #un jour : renvoie [06:00, 06:15, ...]
    for heure in range(6, 10):
        for quart_heure in range(4):
            if quart_heure == 0:
                tranche_horaire.append('0' + str(heure) + ':' + '00')
            else:
                tranche_horaire.append('0' + str(heure) + ':' + str(quart_heure*15))
    for heure in range(10, 24):
        for quart_heure in range(4):
            if quart_heure == 0:
                tranche_horaire.append(str(heure) + ':' + '00')
            else:
                tranche_horaire.append(str(heure) + ':' + str(quart_heure*15))
    return tranche_horaire

class Date:
    def __init__(self, jour, mois):
        self.jour = jour
        self.mois = mois
    def __repr__(self):
        return str(jour) + mois
        
class Heure:
    def __init__(self, t_debut, t_fin):
        self.t_debut = t_debut
        self.t_fin = t_fin
    def __repr__(self):
        return str('t_debut') + str('t_fin')
    
class Edt(Date, Heure):
    def __init__(self):
        self.edt = [[jours[i], ] for i in range(7)] #le tableau emploi du temps [[tranche_horaire lundi], [tranche_horaire mardi], ...]
        self.rdv = {} #input un rdv
    def saisie(self):
        date = Date(input('Date : '))
        heure = Heure(input('Heure :'))
        for (i, jour) in enumerate(jours):
            if date == jour: 
                edt[i] 

