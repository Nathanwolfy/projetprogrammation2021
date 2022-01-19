import emploidutemps as e

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

def edt_medecin_vide(heure_lundi_debut, heure_lundi_fin, heure_mardi_debut, heure_mardi_fin, heure_mercredi_debut, heure_mercredi_fin, heure_jeudi_debut, heure_jeudi_fin, heure_vendredi_debut, heure_vendredi_fin, heure_samedi_debut, heure_samedi_fin):
    if heure_lundi_debut != "" and heure_lundi_fin != "":
        horaire_lundi_debut = e.convert(heure_lundi_debut)
        horaire_lundi_fin = e.convert(heure_lundi_fin)
    else:
        horaire_lundi_debut = None
        horaire_lundi_fin = None
    if heure_mardi_debut != "" and heure_mardi_fin != "":
        horaire_mardi_debut = e.convert(heure_mardi_debut)
        horaire_mardi_fin = e.convert(heure_mardi_fin)
    else:
        horaire_mardi_debut = None
        horaire_mardi_fin = None
    if heure_mercredi_debut != "" and heure_mercredi_fin != "":
        horaire_mercredi_debut = e.convert(heure_mercredi_debut)
        horaire_mercredi_fin = e.convert(heure_mercredi_fin)
    else:
        horaire_mercredi_debut = None
        horaire_mercredi_fin = None
    if heure_jeudi_debut != "" and heure_jeudi_fin != "":
        horaire_jeudi_debut = e.convert(heure_jeudi_debut)
        horaire_jeudi_fin = e.convert(heure_jeudi_fin)
    else:
        horaire_jeudi_debut = None
        horaire_jeudi_fin = None
    if heure_vendredi_debut != "" and heure_vendredi_fin != "":
        horaire_vendredi_debut = e.convert(heure_vendredi_debut)
        horaire_vendredi_fin = e.convert(heure_vendredi_fin)
    else:
        horaire_vendredi_debut = None
        horaire_vendredi_fin = None
    if heure_samedi_debut != "" and heure_samedi_fin != "":
        horaire_samedi_debut = e.convert(heure_samedi_debut)
        horaire_samedi_fin = e.convert(heure_samedi_fin)
    else:
        horaire_samedi_debut = None
        horaire_samedi_fin = None
    Liste_heures = [horaire_lundi_debut, horaire_lundi_fin, horaire_mardi_debut, horaire_mardi_fin, horaire_mercredi_debut, horaire_mercredi_fin, horaire_jeudi_debut, horaire_jeudi_fin, horaire_vendredi_debut, horaire_vendredi_fin, horaire_samedi_debut, horaire_samedi_fin]
    edt = {}
    for i in range(6):
        liste_jour_i = []
        heure_debut = Liste_heures[2*i]
        heure_fin = Liste_heures[2*i+1]
        if heure_debut != None and heure_fin != None:
            if heure_debut < e.Heure(12, 0):
                for heure in range(heure_debut.heure, 12):
                    if heure_debut.minute != 0:
                        for minute in range(heure_debut.minute, 46, 15):
                            liste_jour_i.append(e.Heure(heure, minute))
                    else:
                        for minute in range(0, 46, 15):
                            liste_jour_i.append(e.Heure(heure, minute))
            if heure_fin > e.Heure(13, 0):
                for heure in range(13, heure_fin.heure):
                    for minute in range(0, 46, 15):
                        liste_jour_i.append(e.Heure(heure, minute))
            liste_jour_i.append(heure_fin)
        edt[JOURS[i]] = liste_jour_i
    return edt

edt = edt_medecin_vide("08:00", "19:00", "09:00", "17:00", "08:30", "17:45", "09:45", "18:00", "08:15", "19:00", "", "")
print(edt)