# 3.Find the first non-repeating character

my_string = input("Enter the String: ")
f={}
for i in my_string:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)


for i in my_string:
    if f[i]==1:
        print(i)
        break