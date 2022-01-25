
def strlist_to_list(strlist):
    """(str) -> (list)
    Fonction qui pour un string donné représentant une liste renvoie la liste correspondante.
    """
    return strlist.strip('[]').replace("'", '').split(', ')

def from_string_to_dict(string):
    """(str) -> (dict)
    Fonction qui pour un string donné représentant un dictionnaire renvoie le dictionnaire correspondant.
    """
    if string == '{}':
        return {}
    else:
        version1_str = string.split("{")[1]
        version2_str = version1_str.split("}")[0]
        version3_list = version2_str.split("[")
        version4_list = []
        for elt in version3_list:
            for objet in elt.split("]"):
                version4_list.append(objet)
        version5_list = version4_list[:-1]
        n = len(version5_list)
        version6_list = []
        for i in range (n//2):
            version6_list.append(version5_list[2*i].split("'")[1])
            version6_list.append(version5_list[2*i + 1].split("'"))
        n = len(version6_list)
        version7_list = []
        for i in range (n//2):
            version7_list.append(version6_list[2*i])
            liste_temp = []
            for elt in version6_list[2*i+1]:
                if elt != '' and elt != ', ':
                    liste_temp.append(elt)
            version7_list.append(liste_temp)
        le_dico_enfin = {}
        n = len(version7_list)
        for i in range(n//2):
            le_dico_enfin[version7_list[2*i]] = version7_list[2*i + 1]
        return le_dico_enfin

def from_string_detailsedt_to_dict(string):
    """(str) -> (dict)
    Fonction qui pour une string associée de détails d'un rdv renvoie le dictionnaire correspondant.
    """
    pass

a = "{10:15: ['certificat medical', 'rdv pris', 'Edouard Guehenno'], 10:30: ['certificat medical', 'Aidez-moi svp', 'Laurent Bohn']}"
a.strip('{}')
print(a)
l = a.replace(': ','/').split('], ')
print(l)
for elt in l:
    elt.replace('[','')
    elt.replace(']','')
print(l)