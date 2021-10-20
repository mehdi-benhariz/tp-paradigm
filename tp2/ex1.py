x = int(input("donner un entier \n "))
a = int(input("donner le premier borne "))
b = int(input("donner lae deuxieme borne "))

if (a < x and x < b):
    print("{} est dans l'intervall [{},{}] ".format(x, a, b))
