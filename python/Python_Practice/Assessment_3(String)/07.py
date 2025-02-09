# 7.Count Vowels in a String

str1 = input("Enter the String: ")
count =0
for i in str1:
    if i in 'aeiou':
        count+=1
print(count)