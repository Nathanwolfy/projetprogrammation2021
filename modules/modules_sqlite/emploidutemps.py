JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
MOIS = [i for i in range(1, 13)] #[1 #Janvier, 2 #Février, ...]

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
        if self.heure < 10: #pour faciliter l'accession à la chaine de caractère et faire l'égalité de deux heures
            if self.minute < 10:
                self.repr = '0' + str(self.heure) + ':' + '0' + str(self.minute)
            else:
                self.repr = '0' + str(self.heure) + ':' + str(self.minute)
        else:
            if self.minute < 10: 
                self.repr = str(self.heure) + ':' + '0' + str(self.minute)
            else:
                self.repr = str(self.heure) + ':' + str(self.minute)

    def compare(self, horaire): #compare deux horaires de la classe Heure (<)
        horaire_heure = horaire.heure
        horaire_minute = horaire.minute
        if self.heure == horaire_heure:
            if self.minute < horaire_minute:
                return True
            else:
                return False
        elif self.heure < horaire_heure:
            return True
        else:
            return False

    def __repr__(self): #Heure(8, 0) -> 08:00
        return self.repr

class Motif:
    def __init__(self, motif, duree_rdv):
        self.motif = motif
        self.duree = duree_rdv
    def __repr__(self):
        return str(self.motif)

class Jour: # ex: Lundi 2 Janvier = {06:00 : motif1, 08:45 : carreaux, ...}
    
    def __init__(self, nom_jour, nb_jour, mois):
        self.nom_jour = nom_jour
        self.nb_jour = nb_jour
        self.mois = mois
        self.jour = {}
    
    def un_horaire(self, horaire):
        return self.jour[horaire.repr]

    def ajouter(self, horaire, motif): #motif de la classe Motif
        self.jour[horaire.repr] = motif
        return self.jour 

    def pas_de_rdv(self, heure_debut):
        if self.jour[heure_debut.repr] == '':
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
                Liste_jours_de_la_semaine.append(Jour(JOURS[i], nb_jour, mois_lundi))
            else:
                if mois_lundi == 12:
                    mois_lundi = 1
                else:
                    mois_lundi += 1
                nb_jour = 1
                Liste_jours_de_la_semaine.append(Jour(JOURS[i], nb_jour, mois_lundi))
        self.edt = [Liste_jours_de_la_semaine[i] for i in range(7)] #[{#lundi 06:00 : motif, 06:15 : motif, ...}, {#mardi 06:00 : motif, ...}, ...]
    
    def un_jour_de_edt(self, i):
        return self.edt[i]
    
    def modifier(self, i, heure, motif):
        self.un_jour_de_edt(i).ajouter(heure, motif)
        return self.edt
    
    def edt_creneaux_libres(self, heure_debut, heure_fin):
        edt_creneaux_vides = Edt(self.lundi, self.nb_lundi, self.mois_lundi, self.annee)
        Liste_heure = []
        for jour in range(7):
            for heure in range(heure_debut.heure, heure_fin.heure):
                for minute in range(0, 46, 15):
                    heure_rdv = Heure(heure, minute)
                    try:
                        motif = self.un_jour_de_edt(jour).un_horaire(heure_rdv)
                        duree_rdv = motif.duree
                        duree_boucle = duree_rdv // 15
                        Liste_heure = []
                        heure_i = heure_rdv
                        for i in range(duree_boucle-1):
                            if heure_i.minute == 45:
                                heure_i.heure += 1
                                heure_i.minute = 0
                                heure_i = Heure(heure_i.heure, heure_i.minute)
                            else:
                                heure_i.minute += 15
                                heure_i = Heure(heure_i.heure, heure_i.minute)
                            Liste_heure.append(heure_i.repr)
                    except KeyError:
                        duree_plus_15_min = False
                        for i in range(len(Liste_heure)):
                            if heure_rdv.repr == Liste_heure[i]:
                                duree_plus_15_min = True
                        if duree_plus_15_min == False:
                            edt_creneaux_vides.modifier(jour, heure_rdv, '')
            try:
                self.un_jour_de_edt(jour).un_horaire(heure_fin)
            except KeyError:
                edt_creneaux_vides.modifier(jour, heure_fin, '')
        return edt_creneaux_vides
    
    def __repr__(self):
        return str(self.edt)