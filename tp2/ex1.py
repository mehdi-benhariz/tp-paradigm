x = int(input("donner un entier \n "))
a = int(input("donner le premier borne "))
b = int(input("donner le deuxieme borne "))

if (a < x < b):
    print("{} est dans l'intervall [{},{}] ".format(x, a, b))
else:
    print("{} m'est pas dans l'intervall [{},{}] ".format(x, a, b))
