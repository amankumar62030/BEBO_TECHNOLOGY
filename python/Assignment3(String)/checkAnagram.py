

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1)!=len(s2):
    print("Not anagram")
else:
    a = sorted(s1)
    b = sorted(s2)

    if a==b:
        print("Anagram")
    else:
        print("not anagram")