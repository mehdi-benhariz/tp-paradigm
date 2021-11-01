# while(True):
#     n = int(input("donner la longueur de liste"))
#     if(6 <= n <= 50):
#         break
# D = []
# for i in range(n):
#     x = int(input("donner un entier"))
#     D.append(x)
# acc = D[0]
# R = [acc]
# for x in D[1:]:
#     acc += x
#     R.append(acc)
# print(D)
# print(R)

# n = input("donner un reele")
# decimale = list(n.split(".")[1])
# print(decimale)
N = 2387
A = []
while(True):
    A.append(N % 10)
    N = N//10
    if N == 0:
        break
    print(A, len(A))
