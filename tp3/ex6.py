A, B, C, D, E = [], [], [], [], []

for i in range(3):
    y, z, t1, t2, t3 = [], [], [], [], []
    for j in range(3):
        x = int(input("A[{}][{}]= ".format(i, j)))
        y.append(x)
        x = int(input("B[{}][{}]= ".format(i, j)))
        z.append(x)
        t1.append(y[j]+z[j])
        t2.append(y[j]-z[j])
        t3.append(3*y[j]+10*z[j])
    A.append(y)
    B.append(z)
    C.append(t1)
    D.append(t2)
    E.append(t3)

print(A)
print(B)
print(C)
print(D)
print(E)
