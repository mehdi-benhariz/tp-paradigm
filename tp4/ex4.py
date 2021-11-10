def saisir_noms():
    NOMS = []
    while(True):
        x = input("donner le nom ")
        if x == 'O':
            break
        NOMS.append(x)
    return NOMS


def saisir_temps(NOMS):
    TEMPS = []
    for nom in NOMS:
        for i in range(3):
            x = float(input("Circuit {} de {} ".format(i+1, nom)))
            TEMPS.append(x)
    return TEMPS


def get_temps_moy(TEMPS, NOMS):
    res = {}
    for i in range(len(NOMS)):
        moy = (TEMPS[i]+TEMPS[i+1] + TEMPS[i+2])/3
        res[NOMS[i]] = moy
    return res


def gagnant_circuit(TEMPS, NOMS):
    gagnants = []
    for i in range(int(len(TEMPS), 3)):
        circuit = TEMPS[i::3]
        index = circuit.index(min(circuit))
        print(index)
        gagnants.append(NOMS[index])
        print(NOMS[index])
    return gagnants


NOMS = saisir_noms()
TEMPS = saisir_temps(NOMS)
MOY_TEMPS = get_temps_moy(TEMPS, NOMS)
print(NOMS, TEMPS, MOY_TEMPS)
gagnants = gagnant_circuit(TEMPS, NOMS)
for i in range(len(gagnants)):
    print("gagnant de circuit {} est : {} ".format(i+1, gagnants[i]))

print("le gagnant finale est :{} ".format(min(MOY_TEMPS, key=MOY_TEMPS.get)))
