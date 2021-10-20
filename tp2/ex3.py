montant = 0
nbr_heur = 45
prix_unitaire = 10
if nbr_heur >= 50:
    montant += prix_unitaire*2*(nbr_heur-50)
    montant = 50
if nbr_heur >= 45:
    montant += prix_unitaire*1.75*(nbr_heur-45)
    montant = 45
if nbr_heur >= 40:
    montant += prix_unitaire*1.5*(nbr_heur-40)

print("montant supplimentaire de {} heures est {}".format(nbr_heur, montant))
