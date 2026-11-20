num = int (input("Enter the number of stars :"))

for i in range(1, num+1):

    for j in range(1, i+1):
        print("*", end="")

    space=2*num-2*i
    for k in range(1, space+1):
        print(" ", end="")

    for l in range(1, i+1):
        print("*", end="")

    print()

