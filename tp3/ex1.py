Semaine = ["lundi", "mardi", "mercredi",
           "jeudi", "vendredi", "samedi", "dimanche"]
for day in Semaine:
    print(day)

for i in range(7):
    print(Semaine[i])

A = ['lundi', 'mardi']
B = ['mercredi', 'jeudi']
C = ['vendredi', 'samedi', 'dimanche']

newListe = A+B[1:]+C
print(newListe)
ouvrables = sorted((A+B+C)[:6], reverse=True)
print(ouvrables)
