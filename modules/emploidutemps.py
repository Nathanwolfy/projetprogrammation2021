jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

class Heure:
    def __init__(self, heure, minute):
        self.heure = heure
        self.minute = minute
    def __repr__(self):
        if self.heure < 10:
            if self.minute == 0:
                return '0' + str(self.heure) + ':' + '0' + str(self.minute)
            else:
                return '0' + str(self.heure) + ':' + str(self.minute)
        else:
            if self.minute == 0: 
                return str(self.heure) + ':' + '0' + str(self.minute)
            else:
                return str(self.heure) + ':' + str(self.minute)


class Edt:
    def __init__(self):
        self.edt = [{} for i in range(7)] #[{#lundi 06:00 : motif, 06:15 : motif, ...}, {#mardi 06:00 : motif, ...}, ...]
    def is_empty(self, jour, heure_debut):
        empty = True
        for j in jours:
            if jour == jours[j]:
                if self.edt[j][heure_debut] == '':
                    return empty

class Rdv(Edt):
    def __init__(self, edt):
        super.__init__(edt)
        self.rdv = {}
    def nouveau_rdv(self, jour, horaire, motif): #horaire de la classe heure
        for j in range(7):
            if jour == jours[j]:
                if self.edt.is_empty(jour, horaire):
                    self.edt[j][horaire] = motif
        return self.edt
        



def load_edt(fichier):
    edt = Edt()
    with open(fichier) as file:
        horaire_fin_boucle_while = Heure(23, 45) 
        for (i, horaire) in enumerate(file): #Lundi 22 01 2021 8 00 motif
            H = horaire.split()
            if i == 0:
                heure_journee = int(H[4]) # Heure du début de la journée
                minute_journee = int(H[5]) # Minute du début de la journée
                horaire_debut_boucle_while = Heure(heure_journee, minute_journee)  #Heure du début de la journée
            if i == -1 : # je ne sais pas l'indice de la dernière ligne
                heure_fin_journee = int(H[4]) # Heure de la fin de la journée
                minute_fin_journee = int(H[5]) # Minute de la fin de la journée
                horaire_fin_boucle_while = Heure(heure_fin_journee, minute_fin_journee) # Heure de la fin de la journée du fichier
            jour = H[0]
            heure_rdv = int(H[4])
            minute_rdv = int(H[5])
            heure_debut = Heure(heure_rdv, minute_rdv)
            motif = H[-1]
            for i in range(7):
                if jour == jours[i]:
                    while horaire_debut_boucle_while < heure_debut and horaire_debut_boucle_while <= horaire_fin_boucle_while:
                        edt[i][horaire_debut_boucle_while] = ''
                        if minute_journee == 45:
                            heure_journee += 1
                            minute_debut_journee = 0
                            horaire_debut_boucle_while = Heure(heure_journee + 1, minute_journee)
                        else:
                            minute_debut_journee += 15
                    edt[i][heure_debut] = motif
    return edt

