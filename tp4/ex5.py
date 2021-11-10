def valide(adn):
    return adn != [] and set(adn).issubset(['a', 't', 'g', 'c'])

    # all(item in adn for item in ['a', 't', 'g', 'c'])


def saisi(type="sequence"):
    x = input("donner un {} ADN :".format(type))
    while(not valide(x)):
        x = input("la sequence n'est pas valide, retapez autre fois: ")
    return x


def proportion(chaine, sequence):
    return chaine.count(sequence)


chaine = saisi("chaine")
sequence = saisi()
prop = proportion(chaine, sequence)
print("il y'a {} '{}' dans votre chaine".format(prop, sequence))
