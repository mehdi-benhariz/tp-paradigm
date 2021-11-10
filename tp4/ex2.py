def saisie():
    while(True):
        n = int(input("donner la taille de liste >=2 "))
        if n >= 2:
            return n


def remplir(n):
    liste = []
    for i in range(n):
        while(True):
            x = input("donner la code ")
            if x.upper() in ['A', 'T', 'C', 'G']:
                break
        liste.append(x)
    return liste


def to_ARN(c):
    code = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    return code[c.upper()]


def code_arn(adn):
    arn = []
    for x in adn:
        arn.append(to_ARN(x))
    return arn


n = saisie()
adn = remplir(n)
arn = code_arn(adn)
print(arn)
