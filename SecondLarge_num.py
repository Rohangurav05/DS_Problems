n = list(map(int, input().split()))

first = second = float('-inf')

for i in n:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

if second == float('-inf'):
    print("No second largest element")
else:
    print(second)
