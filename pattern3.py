num=int(input("Enter the star numbers: "))
mid=num//2
for i in range(num):
    for j in range(num): 
        if abs(i-mid)+abs(j-mid)==mid :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()