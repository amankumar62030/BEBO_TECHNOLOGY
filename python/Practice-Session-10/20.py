# 20.	Create a function that takes a list of numbers and removes all duplicates, returning a new list.


# def remove_dup(user_list):
#     dup_list = []
#     for items in user_list:
#         if items not in dup_list:
#             dup_list.append(items)
#     print(dup_list)
# user_list = list(map(int,(input("Enter the elements of list separated by (,): ").split(","))))
# remove_dup(user_list)



n = list(map(int,input("Enter the elements of list:").split(",")))
d =[]
for i in n:
    if i not in d:
        d.append(i)
print(d)

