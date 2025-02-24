# Write a Python program to count the occurrences of each word in a given sentence.
# occurance of each word------------------------------------------
s1 = input("Enter the string:")
f = {}
words = s1.split()

for word in words:
    if word in f:
        f[word] += 1
    else:
        f[word] = 1
print(f)