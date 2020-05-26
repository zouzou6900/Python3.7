# creer une fonction max() qui va renvoyer le resultat le plusd haut parmi les deux valeur
def max(a,b):
    if a>b:
        return a
    else:
        return b
premiere = int(input("Entre la premiere valeur"))
deuxieme = int(input("Entre la deuxieme valeur"))
print("la valeur la plus haute est ",max(premiere,deuxieme))