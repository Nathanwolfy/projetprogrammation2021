
def strlist_to_list(strlist):
    return eval(strlist)

def strlist2_to_list(strlist2):
    resultat = []
    list_temp = eval(strlist2)
    for liste in list_temp:
        resultat.append(eval(liste))
    return resultat

