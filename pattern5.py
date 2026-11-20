num=int(input("Enter the number: "))

for i in range(num):
    for j in range(num):
        if(i+j)%2==0:
            print("1",end=" ")
        else :
            print("0",end=" ")
    print()