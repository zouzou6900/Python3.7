import numpy as np

n = int(input("nombre de ligne : "))
m = int(input("nombre de colone : "))
a = np.arange(n*m).reshape(n,m)
i = 0
while i<n:
    j=0
    while j<m:
        b=int(input("entre B :"))
        a[i][j]= b
        j+=1
    i+=1
print(a)
    
