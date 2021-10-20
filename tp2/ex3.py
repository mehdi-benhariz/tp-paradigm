montant = 0
nbr_heur = 45
prix_unitaire = 10
while(nbr_heur > 49):
    montant += prix_unitaire*2
    nbr_heur -= 1
while(nbr_heur > 44):
    montant += prix_unitaire*1.75
    nbr_heur -= 1
while(nbr_heur > 39):
    montant += prix_unitaire*1.5
    nbr_heur -= 1


print("montant supplimentaire est {}".format(montant))
