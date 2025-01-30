s1 = input("Enter th first String: ")
s2 = input("Enter the second String: ")

if len(s1) != len(s2):
    print(f"{s1} and {s2} are not Anagram")
else:
    a = sorted(s1)
    b = sorted(s2)
    if a == b:
        print(f"{s1} and {s2} are a Anagram")
    else:
        print(f"{s1} and {s2} are not Anagram")