MAX = int(input("donner u max"))
somme = 0
prod = 1
somme_inv = 0
for i in range(1, MAX+1):
    if i % 5 != 0:
        somme += i
        prod *= i
        somme_inv += 1/i

print("somme : {}, produit : {} , somme des inverses : {:.2f} ".format(
    somme, prod, somme_inv))
