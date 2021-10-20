a = int(input("donner a:  "))
b = int(input("donner b:  "))

while(a != b):
    if(a > b):
        a, b = a-b, a
    if(a < b):
        b = b - a
print("le pgcd est : {}".format(a))
