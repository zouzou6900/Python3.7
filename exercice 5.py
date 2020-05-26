nombre = 0
listeRomain = ["M","D","C","L","X","IX","V","IV","III","II","I"]
while nombre < 1 or nombre > 3999:
    nombre = int(input("choisie un nombre entier entre 1 et 3999 : "))
convert = ""
pot=nombre
while pot >0:
    if pot >= 1000:
        pot -= 1000
        convert += listeRomain[0]
    elif pot >= 500:
        pot -= 500
        convert += listeRomain[1]
    elif pot >= 100:
        pot -= 100
        convert += listeRomain[2]
    elif pot >= 50:
        pot -= 50
        convert += listeRomain[3]
    elif pot >= 10:
        pot -= 10
        convert += listeRomain[4]
    elif pot >= 9:
        pot -= 9
        convert += listeRomain[5]
    elif pot >= 5:
        pot -= 5
        convert += listeRomain[6]
    elif pot >= 4:
        pot -= 4
        convert += listeRomain[7]
    elif pot >= 3:
        pot -= 3
        convert += listeRomain[8]
    elif pot >= 2:
        pot -= 2
        convert += listeRomain[9]
    elif pot >= 1:
        pot -= 1
        convert += listeRomain[10]

print(nombre, convert)

      
    