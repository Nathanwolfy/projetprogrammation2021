# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 07:36:47 2021

@author: natha
"""
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

class Heure:
    def __init__(self, heure, minute):
        self.heure = heure
        self.minute = minute
    def __repr__(self):
        return str(self.heure) + ':' + str(self.minute)


class Edt:
    def __init__(self):
        self.edt = [[['']]*18*4]*7 #[[#lundi [06:00, motif], [06:15, motif], ...], [#mardi [06:00], [''], ...], [], [], ...]
    def is_empty(self, jour, heure_debut, motif):
        empty = True
        L_heure, L_minute = heure_debut.split(':')
        heure = L_heure[0]
        minute = L_minute[0]
        for j in jours:
            if jour == jours[j]:
                if self.edt[j][(heure-6)*4+minute] != '':
                    return False
        



def load_edt(fichier):
    edt = Edt()
    with open(fichier) as file:
        for horaire in file: #Lundi 22 01 2021 08 00 motif
            horaire.split()
            jour = horaire[0]
            heure_rdv = int(horaire[4])
            minute_rdv = int(horaire[5])
            heure_debut = Heure(heure_rdv, minute_rdv)
            minute = minute_rdv//15 #06:15 -> minute = 1
            motif = horaire[-1]
            for i in range(7):
                if jour == jours[i]:
                    edt[i][(heure_rdv-6)*4+minute] = heure_debut #[[[''], [''], ..., [08:00]]]
                    edt[i][(heure_rdv-6)*4+minute].append(motif) #[[[''], [''], ..., [08:00, motif]]]
    return edt

