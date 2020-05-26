poids = float(input("Votre poids (en kg) ? "))
taille = float(input("Votre taille (en m) ? "))
imc = poids/(taille*taille)
print("\nIMC = " + str(imc))
if imc > 25.0:
    print("Vous êtes en surpoids.")
elif imc < 18.5:
    print("Voues êtes trop maigre.")
else:
    print("Vous avez une corpulence normale.")