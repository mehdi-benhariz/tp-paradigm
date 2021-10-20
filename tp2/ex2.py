a = int(input("donner a"))
b = int(input("donner b"))

if((a < 0 and b < 0) or (a > 0 and b > 0)):
    print("le produit de {}et {} est positif".format(a, b))
else:
    print("le produit de {}et {} est negatif".format(a, b))
