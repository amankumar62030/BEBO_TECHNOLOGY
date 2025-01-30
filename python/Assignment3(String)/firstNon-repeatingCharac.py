# Find the first non-repeating character


s1 = input("Enter any String: ")

d = {}

for i in s1:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1

for i in s1:
    if d[i] == 1:
        print("The first non-repeating character is:", i)
        break