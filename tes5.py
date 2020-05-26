# Calcul du pgcd de a et b

def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

# fonction de chiffrement affine

def chiffrementAffine(a,b,L):
        alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        x=alphabet.index(L)
        y=(a*x+b)%26
        return alphabet[y]

# Calcul de l'inverse d'un nombre modulo 26

def inverse(a):
        x=0
        while (a*x%26!=1):
                x=x+1
        return x

# Fonction de déchiffrement

def dechiffrementAffine(a,b,L):
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    x=alphabet.index(L)
    y=(inverse(a)*(x-b))%26
    return alphabet[y]
                

# Affichage du mot chiffré

def crypt(M,a,b):
    if (pgcd(a,26)==1):
        mot = []
        for i in range(0,len(M)):
                mot.append(chiffrementAffine(a,b,M[i]))
        return "".join(mot)
    else:
        return "Chiffrement impossible. Veuillez choisir un nombre a premier avec 26."

# Affichage du mot déchiffré

def decrypt(M,a,b):
    if (pgcd(a,26)==1):
        mot = []
        for i in range(0,len(M)):
                mot.append(dechiffrementAffine(a,b,M[i]))
        return "".join(mot)
    else:
        return "Déchiffrement impossible. Le nombre a n'est pas premier avec 26."

print(crypt("MATH",3,10))
print(decrypt("UKPF",3,10))