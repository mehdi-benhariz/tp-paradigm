voy = 0
phrase = input("donner un phrase ")
voyelle = ['a', 'e', 'u', 'o', 'i']

for c in phrase:
    if str.lower(c) in voyelle:
        voy += 1

print(voy)
