age = int(input("Quelle est votre age"))
prix_ado = 7
prix_adu = 12
prix_pop = 5
total = 0

if int(age) < 18:
   total += prix_ado
else:
    total += prix_adu
reponse = input("Souhaiter vous des pop corn ? (oui, non)")

if reponse == "oui":
    total += prix_pop

print("Le prix sera de {}€".format(total))