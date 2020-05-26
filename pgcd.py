a=int(input("saisir le premier nombre ")) 
b=int(input("saisir le deuxieme nombre ")) 
n=a
m=b
while n !=m :
    if n>m :
        n,m=(n-m),n
    elif n < m :
        n,m=n,(m-n) 
print("le PGCD de ",a," et ",b," est : ",n)