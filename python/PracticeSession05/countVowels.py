s1 = input("Enter the String: ")

s1 = s1.lower()

count = 0

for i in s1:
    if i in "aeiou":
        count+=1
print(count)