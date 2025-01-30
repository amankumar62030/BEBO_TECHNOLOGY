
s1 = input("Enter any String: ")
f = {}

for i in s1:
    if i in f:
        f[i]+=1
    else:
        f[i] = 1
print(f)




