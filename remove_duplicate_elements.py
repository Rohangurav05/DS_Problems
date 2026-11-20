arr = list(map(int, input("Enter An Array Element :").split()))
new_arr=[]
for i in arr :
    if i not in new_arr:
        new_arr.append(i)

print("After removing duplicate Elements : ", new_arr)
