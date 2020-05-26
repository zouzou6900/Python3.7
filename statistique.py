from statistics import mean
from random import shuffle
note = [
    1,2,3,
    4,5,6,
    7,8,9
    ]
print(note)
shuffle(note)
print(note)
resultat = mean(note)
print(resultat)