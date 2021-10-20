n = int(input("donner le nombre des entiers a saisir"))
while(n < 1):
    n = int(input("donner le nombre des entiers a saisir"))
somme = 0
for i in range(n):
    x = int(input("donner l'entier {}:  ".format(i)))
    somme += x

print("la somme est {} , le moyen est {}".format(somme, somme/n))
