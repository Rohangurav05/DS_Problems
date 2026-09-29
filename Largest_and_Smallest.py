arr = list(map(int, input("Enter An Array Element :").split()))
large=arr[0]
small=arr[0]
for i in arr :
    if i>large :
        large=i
    if i<small :
        small=i
print("Largest Element : ",large)
print("Smallest Element : ",small)