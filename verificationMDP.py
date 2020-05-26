# Systeme de verification de mot de passe
password = input("Entre votre mot de passe")
password_len = len(password)

#debut des verification
if password_len <= 8:
    print("Votre mot de passe est trop court")
elif 8 < password_len <=12 :
     print("Votre mot de passe est moyen")
else:
     print("Votre mot de passe est parfait")
    