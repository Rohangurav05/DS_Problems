arr = list(map(int, input("Enter An Array Element :").split()))

countodd=0
counteven=0

for i in arr :
    if i%2==0 :
        counteven=counteven+1
    if i%2!=0 :
        countodd=countodd+1
print("Even numbers are : ",counteven) 
print("Odd numbers are : ",countodd)   