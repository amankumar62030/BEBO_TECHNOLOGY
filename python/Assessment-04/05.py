# WAP to remove minimum and maximum values from the set.

# s1 = {10,20,30,56,40}
#
# min_value = float('inf')
# max_value = float('-inf')
#
# for i in s1:
#     if i<min_value:
#         min_value = i
#     if i > max_value:
#         max_value = i
#
# print(min_value,max_value)
#
# s1.remove(min_value)
# s1.remove(max_value)
# print(s1)

sett = {10,20,30,40}
min_val = float('inf')
max_val = float('-inf')

for i in sett:
    if i>max_val:
        max_val=i

    if i<min_val:
        min_val=i
print(max_val,min_val)

sett.remove(min_val)
sett.remove(max_val)
print(sett)

