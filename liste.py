#creation d une liste
liste_fruit = ["ananas","appel","orange"]
print(liste_fruit)
# premiere vbaleur de la liste
print(liste_fruit[0])
# afficher la derniere valeur de liste
print(liste_fruit[len(liste_fruit) - 1 ])
#modifier une valeur dans la liste
liste_fruit[0] = "ananass"
print(liste_fruit)
#insert une valeur dans la liste apres tel valeur
liste_fruit.insert(1,"pear")
print(liste_fruit)
#modifier plusieur valeur
liste_fruit[2:3] = "pomme", "poire"
print(liste_fruit)
#ajouter un element a la liste
liste_fruit.append("betrave")
print(liste_fruit)
# ajouter plusieur element a la liste
liste_fruit.extend(["banane","haricot"])
print(liste_fruit)
# suprime un element de la liste par son index
del liste_fruit[3]
print(liste_fruit)
# ou
liste_fruit.pop(4)
print(liste_fruit)
#supprimer pas la valeur
liste_fruit.remove("ananass")
print(liste_fruit)
#vider la liste totalement
del liste_fruit[:]
#ou
liste_fruit.clear()
print(liste_fruit)