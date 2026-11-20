num=int(input("Enter the num:"))

for i in range(num) :
    #print(" "*(num-i+1),end="")
    for j in range(1,num-i+1):
        print("  ",end="")
        
    for j in range (2*i+1) :
        if (i==num-1 or j==0 or j==2*i) : 
            print(chr(65+j), end=" ")
        else :
            print(" ",end=" ")
    print()
