def verification(annee):
    if((annee%4)==0 and (annee%100!=0) or annee%400==0):
       return print("L'annee est une annee bissextile!")
    else:
       return print("L'annee n'est pas une annee bissextile!")


annee = int(input("Entrez l annee a verifier:"))
verification(annee)