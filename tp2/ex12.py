n = int(input("donner un entier"))

fact = 1

# 1er methode
for i in range(2, n+1):
    fact *= i

# 2eme methode
# while(n > 1):
#     fact *= n
#     n -= 1
print("le factoriale est {} ".format(fact))
