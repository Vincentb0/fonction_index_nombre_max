"""
Fonction qui renvoi l'index de l'élément ayant la valeur
plus élevée dans la liste transmise en argument.
"""

serie = [5, 8, 2, 1, 9, 3, 6, 7]

def index_max(liste):
    longueur_liste = len(liste)
    max = liste[0]
    i = 0
    index = 0

    while i < longueur_liste:
        valeur_max = liste[i]
        if valeur_max > max:
            max = valeur_max
            index = liste.index(max)
        i += 1
    return index

index_nombre_max = index_max(serie)
print("L'index du nombre le plus grand est :", index_nombre_max)


"""
La fonction renvoi :

L'index du nombre le plus grand est : 4
"""