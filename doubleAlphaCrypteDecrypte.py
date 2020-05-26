def crypter_alea(msg):
    cle = 'HYLUJPVREAKBNDOFSQZCWMGITX'
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for caractere in msg:
        indice = alpha.find(caractere)
        res += cle[indice]
    return res

def decrypter_alea(msg):
    cle = 'HYLUJPVREAKBNDOFSQZCWMGITX'
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for caractere in msg:
        indice = cle.find(caractere)
        res += alpha[indice]
    return res

print(crypter_alea("ABCDEFZ"))
print(decrypter_alea("HYLUJPX"))