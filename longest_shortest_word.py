s=input("Enter the string :")
words=s.split()
long=words[0]
short=words[0]

for word in words :
    if len(word) > len(long) :
        long=word
    if len(word) < len(short):
        short=word

print("Longest word :",long)
print("Shortest word :",short)