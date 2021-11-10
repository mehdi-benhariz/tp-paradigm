Nb_jour, Mois = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31], ["January", "February", "March", "April", "May", "June", "July ",
                                           "August", "September ", "October", "November", "December"]


def Mois_jours(Nb_jour, Mois):
    res = {}
    for j, m in zip(Nb_jour, Mois):
        res[m] = j
    return res


def ordre_Mois(Mois):
    res = {}
    for i, m in zip(range(12), Mois):
        res[i] = m
    return res


def valide(obs):
    j, m = obs[0], obs[1]

    mo, mj = ordre_Mois(Mois), Mois_jours(Nb_jour, Mois)
    return j <= mj[mo[m-1]]


def Num_jour(obs):
    j, m, num_jour, i = obs[0], obs[1], 0, 0
    if valide(obs):
        while(i < m-1):
            num_jour += Nb_jour[i]
            i += 1
        return num_jour + j


def avant_qui(obs1, obs2):
    return Num_jour(obs1) < Num_jour(obs2)


def selection(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i+1, len(l)):
            if avant_qui(l[j], l[min_idx]):
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l


print(avant_qui([16, 1, 14], [12, 2, 14]))
l = [[12, 2, 14], [16, 1, 14], [12, 7, 14], [12, 5, 14], [20, 2, 14]]
l = selection(l)
print(Num_jour(l[0]))
print(l)
