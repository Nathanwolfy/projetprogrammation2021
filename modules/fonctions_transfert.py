
def strlist_to_list(strlist):
    return strlist.strip('[]').replace("'", '').split(', ')

def strlist2_to_list(strlist2):
    resultat = []
    l1 = strlist2.strip('[]').split("], [")
    for sublist in l1:
        resultat.append(sublist.replace("'","").split(", "))
    return resultat