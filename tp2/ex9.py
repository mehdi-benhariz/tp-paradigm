import math
x = 0
while(True):
    x = int(input("donner un entier postive"))
    if(x > 0):
        break

sum_div = 0
for i in range(1, math.ceil(math.sqrt(x))+1):
    if(x % i == 0):
        sum_div += i

if sum_div == x:
    print("nombre parfait")
else:
    print("n'est pas un nombre parfait")
