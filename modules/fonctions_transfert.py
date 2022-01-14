
def strlist_to_list(strlist):
    return strlist.strip('[]').replace("'", '').split(', ')

def strlist2_to_list(strlist2):
    resultat = []
    l1 = strlist2.strip('[]').split("], [")
    for sublist in l1:
        resultat.append(sublist.replace("'","").split(", "))
    return resultat

def from_string_to_dict(string):
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
