from random import randint

a = randint(0, 100)
print(a)
while(True):
    x = int(input("devinez un nombre!  "))
    if(x < a):
        print("trop petit")
    elif x > a:
        print("trop grand")
    else:
        break

print(" bravo ! le nombre est {}".format(a))
