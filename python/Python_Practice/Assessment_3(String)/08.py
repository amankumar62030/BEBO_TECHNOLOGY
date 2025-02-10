# 8.Write a Python function to find the longest word in a given sentence.

str1 = input("Enter the sentence: ")
word = str1.split()
print(word)

d = {}
for i in word:
    d[i] = len(i)
# print(d)

m = max(d.values())

for key,value in d.items():
    if value==m:
        print(key,value)
