num=int(input("Enter the star numbers: "))

for i in range(num) :
    for j in range (num) :
      if i==num//2 or j==num//2 :
         print("*",end="")
      else :
         print(" ",end="")
    print()