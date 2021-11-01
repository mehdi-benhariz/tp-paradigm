X, Y = {'a', 'b', 'c', "d"}, {'s', 'b', 'd'}
print(X, Y)
if 'c' in X:
    print("c in X")
else:
    print("c n'est pas in X")

if 'a' in Y:
    print("a in Y")
else:
    print("a n'est pas in Y")
print(X-Y)
print(Y-X)

print(X | Y)
print(X & Y)
