print("donner l'heure")
while(True):
    h = int(input("svp donner l'heure entre 0 et 23    "))
    if(0 <= h <= 23):
        break
while(True):
    m = int(input("svp donner les minutes entre 0 et 59    "))
    if(0 <= m <= 59):
        break

while(True):
    s = int(input("svp donner les seconde entre 0 et 59    "))
    if(0 <= s <= 59):
        break

if (s == 59):
    if(m == 59):
        if(h == 23):
            h = 00
        else:
            h += 1
        m = 0
    else:
        m += 1
    s = 0
else:
    s += 1

print("{:02d}:{:02d}:{:02d}".format(h, m, s))
