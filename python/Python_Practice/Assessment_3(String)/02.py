# 2.Count the frequency of characters in a string

my_string = input("Enter the String: ")

f ={}

for i in my_string:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)
