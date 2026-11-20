arr = list(map(int, input("Enter An Array Element :").split()))
result=[]
for i in arr :
    if i!=0 :
        result.append(i)

result=result+[0]*(len(arr)-len(result))

print("Array", result)