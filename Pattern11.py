num = int(input("Enter the number: "))

for i in range(1, num + 1):

    for j in range(num - i):
        print(" ", end="")

    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == num:
            print("*", end="")
        else:
            print(" ", end="")

    print()
