n = int(input("donner un entier n: "))

for i in range(2, n):
    if(n % i == 0):
        print("{} n'est pas premier".format(n))
        break
if i == n:
    print("{} est  premier".format(n))
