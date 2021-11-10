from random import randint
from math import ceil, sqrt
from itertools import permutations


def saisie():
    while(True):
        n = int(input("donner la taille de tableau >=2 "))
        if n >= 2:
            return n


def remplir(n):
    liste = []
    for i in range(n):
        x = randint(100, 999)
        liste.append(x)
    return liste


def est_premier(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def combination_premier(elt):
    x, y, z = elt//100, int(str(elt)[1]), elt % 10
    comb = permutations([x, y, z])

    for i in set(comb):
        a = int(''.join(map(str, i)))
        print(a)
        if (not est_premier(a)):
            return False
    return True


def est_premier_absolue(l):
    res = []
    for elt in l:
        if(combination_premier(elt)):
            res.append(elt)
    return res


n = saisie()
liste = remplir(n)
res = est_premier_absolue(liste)
print(combination_premier(337))
for x in res:
    print("{} res est premier absolu \n ".format(x))
