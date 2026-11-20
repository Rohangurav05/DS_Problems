s=input("Enter the string :" )
words=s.split()

for word in words :
    for i in range(len(word)-1,-1,-1):
        print(word[i],end="")
    print(end=" ")