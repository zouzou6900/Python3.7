print("Note 1 - ", end=" ") 
note=float(input()) 
nb=0
S=0
while note>=0:
    nb+=1
    S=note
    print("Note ",(nb+1), end=" ") 
    note=float(input())
if nb>0:
    print("moyenne de ",nb," notes est ",S/nb)