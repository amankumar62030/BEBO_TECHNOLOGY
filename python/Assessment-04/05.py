# WAP to remove minimum and maximum values from the set.

s1 = {10,20,30,56,40}

min_value = float('inf')
max_value = float('-inf')

for i in s1:
    if i<min_value:
        min_value = i
    if i > max_value:
        max_value = i

print(min_value,max_value)

s1.remove(min_value)
s1.remove(max_value)
print(s1)



