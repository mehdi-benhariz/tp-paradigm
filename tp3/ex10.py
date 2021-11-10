texte = input("donner une ligne de text:  \n")
freq = {}
texte = texte.replace(" ", "")
for c in texte:
    if c in freq.keys():
        freq[c] += 1
    else:
        freq[c] = 1

print(freq)
for key, value in zip(freq.keys(), freq.values()):
    print("{} : %{:.2f}".format(key, 100 * value/len(texte)))
