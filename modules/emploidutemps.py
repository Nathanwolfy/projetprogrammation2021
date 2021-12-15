jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois = [i for i in range(1, 13)] #[1 #Janvier, 2 #Février, ...]

def nb_jours_dans_un_mois(mois, annee): 
    if mois == 2: #Février
        if annee % 4 == 0:
            return 29 #année bissextile
        else:
            return 28 #année non bissextile
    elif mois%2 == 0:
        return 31
    return 30


class Heure: 

    def __init__(self, heure, minute):
        self.heure = heure
        self.minute = minute
    
    def compare(self, horaire): #compare deux horaires de la classe Heure (<)
        horaire_heure = horaire.heure
        horaire_minute = horaire.minute
        if self.heure <= horaire_heure:
            if self.minute <= horaire_minute:
                return True
            else:
                return False
        else:
            return False
    
    def meme_heure(self, horaire):
        if self.heure == horaire.heure and self.minute == horaire.minute:
            return True
    
    def __repr__(self): #Heure(8, 0) -> 08:00
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
    
    def un_horaire(self, horaire):
        print(self.jour)
        return self.jour[horaire]

    def ajouter(self, horaire, motif):
        self.jour[horaire] = motif
        return self.jour 

    def pas_de_rdv(self, heure_debut):
        print(self.jour)
        print(heure_debut)
        if self.jour[heure_debut] == '':
            return True
    
    def nouveau_rdv(self, horaire, motif): #horaire de la classe Heure
        if self.pas_de_rdv(horaire):
            self.ajouter(horaire, motif)
            return self.rdv
    
    def convert_list(self):
        return self.jour.items()

    def __repr__(self):
        return str(self.jour)


class Edt: # Une semaine, juste besoin du lundi
    
    def __init__(self, lundi, nb_lundi, mois_lundi, annee): #ex : Lundi 2 Janvier (=01)
        self.annee = annee
        self.lundi = lundi
        self.nb_lundi = nb_lundi
        self.mois_lundi = mois_lundi
        Lundi = Jour(lundi, nb_lundi, mois_lundi)
        Liste_jours_de_la_semaine = []
        Liste_jours_de_la_semaine.append(Lundi)
        nb_jour = nb_lundi
        for i in range(6): #[Lundi 2 Janvier, Mardi 3 Janvier, Mercredi 4 Janvier, ...]
            if nb_jour < nb_jours_dans_un_mois(mois_lundi, self.annee):
                nb_jour += 1
                Liste_jours_de_la_semaine.append(Jour(jours[i], nb_jour, mois_lundi))
            else:
                if mois_lundi == 12:
                    mois_lundi = 1
                else:
                    mois_lundi += 1
                nb_jour = 1
                Liste_jours_de_la_semaine.append(Jour(jours[i], nb_jour, mois_lundi))
        self.edt = [Liste_jours_de_la_semaine[i] for i in range(7)] #[{#lundi 06:00 : motif, 06:15 : motif, ...}, {#mardi 06:00 : motif, ...}, ...]
    
    def un_jour_de_edt(self, i):
        return self.edt[i]
    
    def modifier(self, i, heure, motif):
        self.un_jour_de_edt(i).ajouter(heure, motif)
        return self.edt
    
    def is_empty(self, i, heure_debut):
        if self.un_jour_de_edt(i).pas_de_rdv(heure_debut):
            return True
    
    def __repr__(self):
        return str(self.edt)


def load_edt(fichier):
    with open(fichier) as file:
        for (i, horaire) in enumerate(file): #Lundi 22 01 2021 8 00 motif
            H = horaire.split()
            if i == 0:
                edt = Edt(H[0], int(H[1]), int(H[2]), int(H[3]))
                heure_journee = int(H[4]) # Heure du début de la journée
                minute_journee = int(H[5]) # Minute du début de la journée
                horaire_debut_boucle_while = Heure(heure_journee, minute_journee)  #Heure du début de la journée
            jour = H[0]
            heure_rdv = int(H[4])
            minute_rdv = int(H[5])
            heure_debut = Heure(heure_rdv, minute_rdv) # Heure du rdv
            motif = H[-1]
            for j in range(7):
                if jour == jours[j]:
                    while horaire_debut_boucle_while.compare(heure_debut): #hor_deb_bou_whi <= heure_debut
                        if minute_journee == 45:
                            heure_journee += 1
                            minute_journee = 0
                            horaire_debut_boucle_while = Heure(heure_journee, minute_journee)
                        else:
                            minute_journee += 15
                            horaire_debut_boucle_while = Heure(heure_journee, minute_journee)
                    edt.modifier(j, heure_debut, motif)
    return edt

def edt_creneaux_libres(edt, heure_debut, heure_fin): #edt de la classe Edt, heure_debut = heure début de la journée arbitraire, heure_fin = heure fin journée arbitraire
    edt_creneaux_vides = Edt(edt.lundi, edt.nb_lundi, edt.mois_lundi, edt.annee)
    for j in range(7):
        els = list(edt.un_jour_de_edt(j).convert_list()) #convertit dictionnaire en list, {"avion": "plane", "blabla": "pomme"} -> [("avion", "plane"), ("blabla", "pomme")]
        if len(els) == 0:
            for i in range():
        for i in range(len(els)):
            heure_debut = els[i][0]
            horaire_debut_boucle_while = heure_debut #La journée commence à 8h
            heure_journee = heure_debut.heure
            minute_journee = heure_debut.minute
            while horaire_debut_boucle_while.compare(heure_debut) and horaire_debut_boucle_while.compare(heure_fin):
                if not horaire_debut_boucle_while.meme_heure(heure_debut):
                    edt_creneaux_vides.modifier(j, horaire_debut_boucle_while, '')
                if minute_journee == 45:
                    heure_journee += 1
                    minute_journee = 0
                    horaire_debut_boucle_while = Heure(heure_journee, minute_journee)
                else:
                    minute_journee += 15
                    horaire_debut_boucle_while = Heure(heure_journee, minute_journee) 
    return edt_creneaux_vides      

if __name__ == '__main__':

    edt = load_edt('Test_edt2.txt')
    print(edt)
    edt_libre = edt_creneaux_libres(edt, Heure(8, 0), Heure(22, 0))
    print(edt_libre)
