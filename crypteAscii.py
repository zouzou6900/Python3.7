msg=('abc')
cle=-3                    

def crypte(msg, cle):
    phrase = list(msg)
    mot=[]
    tab=[]
    code=[]
    for i in phrase:  
        num=ord(i)
        tab.append(num)
        mot.append(num+cle)    
  
    for j in mot:
        lettre = chr(j)
        code.append(lettre)
     
    print("".join(code))
     
crypte(msg, cle)