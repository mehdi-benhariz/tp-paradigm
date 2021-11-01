MAX = int(input("donner u max"))
somme, prod, somme_inv = 0, 1, 0
for i in range(1, MAX+1):
    if i % 5 != 0:
        somme += i
        prod *= i
        somme_inv += 1/i

print("somme : {}, produit : {} , somme des inverses : {:.2f} ".format(
    somme, prod, somme_inv))
