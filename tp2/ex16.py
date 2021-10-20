for i in range(4):
    print("*"*4)

for i in range(1, 6):
    print("*"*i)

for i in range(4):
    if(i == 0 or i == 3):
        print("*"*4)
    else:
        print("*  *")

for i in range(1, 6):
    if i == 5 or i == 1:
        print("*"*i)
    else:
        print("*"+" "*(i-2)+"*")
