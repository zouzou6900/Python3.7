import math
import random
import time
import sys

toolbar_width = 80

minPrime = 10
maxPrime = 1000

message = int
d = 0.1
p = int
q = int
e = int
r = int
answer = int
messageAscii = list
result = int
toolbar_width = 10

encryptedMessage = 0
decryptedMessage = 0

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False
    return n>1

def keyGen():
    global p, q, e, r
    p = random.choice([m for m in range(minPrime, maxPrime) if isPrime(m)])
    q = random.choice([m for m in range(minPrime, maxPrime) if (isPrime(m)) & (m != p)])
    e = random.choice([m for m in range(minPrime, maxPrime) if (isPrime(m)) & (m > p) & (m > q)]) #clé d'encryptage
    r = p * q
    return (e, r)

def getDecryptKey(randomChoiceP, randomChoiceQ, publicKeyE): #ok
    z = (randomChoiceP - 1) * (randomChoiceQ - 1)
    n = 1
    global d
    while d != int(d):
        d = ((z * n) + 1)/ publicKeyE
        n += 1
    return d

def encrypt(messageToEncrypt, publicKeyE, publicKeyR): #ok
    global encryptedMessage 
    encryptedMessage = ((messageToEncrypt ** publicKeyE) % publicKeyR)
    return encryptedMessage

def encryptList(listToEncrypt, publicKeyE, publicKeyR):
    encryptedList = [encrypt(x, publicKeyE, publicKeyR) for x in listToEncrypt]
    return encryptedList

def decrypt(messageToDecrypt, publicKeyR, secretKeyD): #ok
    global decryptedMessage
    decryptedMessage = ((messageToDecrypt ** secretKeyD) % publicKeyR)
    return decryptedMessage

def decryptList(listToDecrypt, publicKeyR, secretKeyD):
    decryptedList = [decrypt(x, publicKeyR, secretKeyD) for x in listToDecrypt]
    return decryptedList

def getOrd(message):
    messageList = list(message)
    result = [ord(x) for x in messageList]
    return result

def getChr(message):
    chrList = [chr(x) for x in message]
    result = "".join(chrList)
    return result

answer = input("//Voulez-vous générer vos clés? (Y/N) :")
if (answer == "Y"):
    keyGen()
    print("//Ok ! Voici donc vos clés RSA générées aléatoirement : ( RSA,",e,",",r,")")
    message = input("//Entrez maintenant le message que vous voulez encrypter : ")
    if (len(message) <= 80):
        messageInt = getOrd(message)
        print("//Admettons que votre message est",messageInt,", je vais encrypter votre message")
        encryptedList = encryptList(messageInt, e, r)
        print("//Voici le message encrypté",encryptedList)
        getDecryptKey(p, q, e)
        print("//La clé de decryptage est :",int(d))
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))
        for i in range(toolbar_width):
            decryptedList = decryptList(encryptedList, r, int(d))
            sys.stdout.write("#")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        print("//Voici le message décrypté :",decryptedList)
        messageChr = getChr(decryptedList)
        print("//Et le voici sous forme finale :",messageChr)
    else:
        print("Le message dépasse 80 caractères ! Il faudra raccourcir votre message !")
elif (answer == "N"):
    print("Dommage !")