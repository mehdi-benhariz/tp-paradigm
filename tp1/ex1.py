x = int(input("donner x: \n"))
y = int(input("donner y: \n"))

print("x={:>4d} , y={:>4d}".format(x, y))
x, y = y, x
print("x={:>4d} , y={:>4d}".format(x, y))
