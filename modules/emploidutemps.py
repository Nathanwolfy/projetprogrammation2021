jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

class Heure:
    def __init__(self, heure, minute):
        self.heure = heure
        self.minute = minute
    def compare(self, horaire): #compare deux horaires de la classe Heure
        horaire_heure = horaire.heure
        horaire_minute = horaire.minute
        if self.heure < horaire_heure:
            return True
        elif self.heure > horaire_heure:
            return False
        else:
            if self.minute < horaire_minute:
                return True
            else:
                return False
    def __repr__(self):
        if self.heure < 10:
            if self.minute < 10:
                return '0' + str(self.heure) + ':' + '0' + str(self.minute)
            else:
                return '0' + str(self.heure) + ':' + str(self.minute)
        else:
            if self.minute < 10: 
                return str(self.heure) + ':' + '0' + str(self.minute)
            else:
                return str(self.heure) + ':' + str(self.minute)

class Jour: # ex: Lundi 2 Janvier = {06:00 : motif1, 08:45 : carreaux, ...}
    def __init__(self, nom_jour, nb_jour, mois):
        self.nom_jour = nom_jour
        self.nb_jour = nb_jour
        self.mois = mois
        self.jour = {}
    def pas_de_rdv(self, le_jour, heure_debut): #le_jour de la classe Jour
        if self.nom_jour == le_jour.nom_jour and self.nb_jour == le_jour.nb_jour and self.mois == le_jour.mois:
            if self.jour[heure_debut] == '':
                return True
    def nouveau_rdv(self, le_jour, horaire, motif): #horaire de la classe heure
        if self.nom_jour == le_jour.nom_jour and self.nb_jour == le_jour.nb_jour and self.mois == le_jour.mois:
            if self.pas_de_rdv(le_jour, horaire):
                self.jour[horaire] = motif
                return self.rdv
    def __repr__(self):
        return str(self.jour)

class Semaine(Jour):
    def __init__(self, )

class Edt(Jour): # Une semaine
    def __init__(self, semaine): # numéro de la semaine, ex : semaine 14 = 14
        super.__init__()
        self.semaine = semaine
        self.edt = [self.jour for i in range(7)] #[{#lundi 06:00 : motif, 06:15 : motif, ...}, {#mardi 06:00 : motif, ...}, ...]
    def is_empty(self, le_jour, heure_debut):
        for j in jours:
            if le_jour == jours[j]:
                if self.edt[j].pas_de_rdv(le_jour, heure_debut):
                    return True
    def __repr__(self):
        return str(self.edt)


def load_edt(fichier):
    edt = Edt()
    with open(fichier) as file:
        for (i, horaire) in enumerate(file): #Lundi 22 01 2021 8 00 motif
            H = horaire.split()
            if i == 0:
                heure_journee = int(H[4]) # Heure du début de la journée
                minute_journee = int(H[5]) # Minute du début de la journée
                horaire_debut_boucle_while = Heure(heure_journee, minute_journee)  #Heure du début de la journée
            jour = H[0]
            heure_rdv = int(H[4])
            minute_rdv = int(H[5])
            heure_debut = Heure(heure_rdv, minute_rdv) # Heure du rdv
            motif = H[-1]
            for i in range(7):
                if jour == jours[i]:
                    while horaire_debut_boucle_while.compare(heure_debut):
                        edt[i].jour[horaire_debut_boucle_while] = ''
                        if minute_journee == 45:
                            heure_journee += 1
                            minute_debut_journee = 0
                            horaire_debut_boucle_while = Heure(heure_journee, minute_journee)
                        else:
                            minute_debut_journee += 15
                    edt[i].jour[heure_debut] = motif
                    print(edt)
    return edt

if __name__ == '__main__':

    edt = load_edt('Test_edt.txt')
    print(edt)
