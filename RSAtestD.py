import math
import random
import time
import sys

valMin=1
valMax=1000
message = int
d = 0.1
p = int
q = int
e = int
r = int
toolbar_width = 10
encrypte = 0
decrypte = 0

def mode():
    while True:
        print('Voulez vous cryptez (c) ou decryptez (d) votre message?')
        mode = input().lower()
        if mode in 'c d'.split():
            return mode
        else:
            print('Entrez un choix "c" ou "d".')

def msg():
     message = input("Entrez le message : ")
     return message

def verif(nombre):
    for i in range(2, int(math.sqrt(nombre)+1)):
        if nombre % i == 0:
            return False
    return nombre>1

def key():
    global p, q, e, r
    p = random.choice([key for key in range(valMin, valMax) if verif(key)])
    print('p :', p)
    q = random.choice([key for key in range(valMin, valMax) if (verif(key)) & (key != p)])
    print('q :',q)
    e = random.choice([key for key in range(valMin, valMax) if (verif(key)) & (key > p) & (key > q)])
    print('e :',e)
    r = p * q
    print('r :',r)
    return (e, r)

def encrypt(message, keyE , keyR):
    global encrypte
    encrypte = ((message ** keyE) % keyR)
    return encrypte

def decrypt(messageToDecrypt, publicKeyR, secretKeyD): #ok
    global decrypte
    decrypte = ((messageToDecrypt ** secretKeyD) % publicKeyR)
    return decrypte

def listeEncrypte(liste, keyE, keyR):
    encrypte = [encrypt(x, keyE, keyR) for x in liste]
    return encrypte

def listeDecrypte(listToDecrypt, keyR, keyD):
    decryptedList = [decrypt(x, keyR, keyD) for x in listToDecrypt]
    return decryptedList

def ordre(message):
    liste = list(message)
    result = [ord(x) for x in liste]
    return result

def getChr(message):
    chrList = [chr(x) for x in message]
    result = "".join(chrList)
    return result

def getDecryptKey(randomChoiceP, randomChoiceQ, publicKeyE):
    z = (randomChoiceP - 1) * (randomChoiceQ - 1)
    n = 1
    global d
    while d != int(d):
        d = ((z * n) + 1)/ publicKeyE
        n += 1
    return d

mode = mode()

if mode == "c":
    key()
    print("Vos clés RSA générées aléatoirement : ( RSA,",e,",",r,")")
    msg = msg()
    if len(msg) <= 80:
        message = ordre(msg)
        print("Votre message recomposée en nombres ascii :\n",message)
        encrypte = listeEncrypte(message, e, r)
        print("Voici le message encrypté",encrypte)
        getDecryptKey(p, q, e)
        print("La cle de decryptage est :",int(d))
    else:
        print("Le message dépasse 80 caractères.")
else:
    msg = msg()
    msg = msg.replace(' ','')
    msg = msg.replace('[','')
    msg = msg.replace(']','')
    encryptedList = msg.split(",")
    d = int(input("Entre la cle de decryptage"))
    r = int(input("Entre la cle r"))
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for i in range(toolbar_width):
        decryptedList = listeDecrypte(encryptedList, r, int(d))
        sys.stdout.write("#")
        sys.stdout.flush()
    sys.stdout.write("]\n")
    print("//Voici le message décrypté :",decryptedList)
    messageChr = getChr(decryptedList)
    print("//Et le voici sous forme finale :",messageChr)
