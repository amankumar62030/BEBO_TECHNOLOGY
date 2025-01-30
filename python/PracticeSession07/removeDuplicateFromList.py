# Write a function called remove_duplicates that takes a list of integers and returns a new list with duplicates removed while maintaining the original order.

user_list = list(map(int,(input("Enter the elements of list separated by (,): ").split(","))))
# dup_list = []
#
# for items in user_list:
#     if items not in dup_list:
#         dup_list.append(items)
# print(dup_list)


i = 0
while(i<len(user_list)):
    j = i+1
    while(j<len(user_list)):
        if user_list[i]==user_list[j]:
            user_list.pop(j)
        else:
            j=j+1
    i=i+1

print(user_list)







