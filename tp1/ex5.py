TVA = 0.196
nbr_article = 5
prix_unitaire = 42.15
prix_ttc = nbr_article*prix_unitaire*(1+TVA)
print("le prix TTC est {:.2f} ".format(prix_ttc))
