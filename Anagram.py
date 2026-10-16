s1 = input().lower()
s2 = input().lower()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
