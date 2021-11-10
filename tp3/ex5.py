import math
carres, cubes, puissance, sinus = [], [], [], []
for i in range(20, 41):
    carres.append(i**2)
    cubes.append(i**3)
for i in range(6, 15):
    puissance.append(i**5)
for i in range(0, 91, 5):
    puissance.append(round(math.asin(i), 2))
