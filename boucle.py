#  boucle for pour une valeur de 1 depart juasqu a une valeur d arrive 5
for num_client in range(1,6):
    print("vous est le client n°", num_client)
# boucle for each a partir du liste
emails = ["pat@hotmail.fr","fredfd@gmail.com","jim@carre.io","invalid@bizz.org"]
for email in emails:
    print("email envoyé à:", email)
# boucle while pendant que c est en desous de 24 mois sa continue   
nbre = 2500
mois = 0
while mois <= 24:
      nbre *= 1.10
      print("resultat {}".format(nbre))
      mois += 1
    
