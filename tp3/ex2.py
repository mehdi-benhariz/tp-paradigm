n = int(input("donner la longueur de liste"))
L = []
somme = 0
max = -9999999
min = 9999999
for i in range(n):
    x = int(input("donner un entier"))
    L.append(x)
    n -= 1
    somme += x
    max = max if max > x else x
    min = min if min < x else x
print("somme : {} , min : {}  , max : {} ".format(somme, min, max))
