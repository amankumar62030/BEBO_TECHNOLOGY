# 10.Write a Python program to count the occurrences of each word in a given sentence.

my_string = input("Enter the String: ")
word = my_string.split()
f ={}
for i in word:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)
