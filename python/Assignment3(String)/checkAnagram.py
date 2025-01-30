

s1 = input("Enter first String: ")
s2 = input("Enter second String: ")

if len(s1)!=len(s2):
    print("Not Anagram..")

else:
    a = sorted(s1)
    b = sorted(s2)
    if(a==b):
        print("Anagram..")
    else:
        print("Not Anagram..")