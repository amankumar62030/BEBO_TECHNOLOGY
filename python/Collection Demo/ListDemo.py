# A list is a collection which is ordered and changeable
# it is mutable


#----------------------- How to create a list
myList1 = [10,11,12,13,14]
mylist2 = ["Apple", "Mango","Cherry"]
mylist3 = ["Apple", 34.5, True, 44]
mylist4 = list()     #empty list

print(myList1)
print(mylist2)
print(mylist3)
print(mylist4)

# ---------------Accessign the elements of list------------------
print(mylist2[0])       #apple
print(mylist2[-1])      #cherry
print(mylist2[2])       #cherry


# ------------------Range of Index..............
mylist = ["apple", "mango","kiwi","orange","melon","mango"]
print(mylist[1:3])
print(mylist[2:5])
print(mylist[-4:-1])



# ----------------------change item value------------------
mylist = ["apple", "mango","kiwi","orange","melon","mango"]

mylist[0] = "Banana"
print(mylist)


# ---------------reading list items using loop--------------------------
mylist = ["apple", "mango","kiwi","orange","melon","mango"]

for i in mylist:
    print(i)


# -------------------check if items is present or not--------------------

mylist6 = ["apple", "mango", "kiwi", "orange", "melon", "mango"]

if "apple" in mylist6:
    print("apple is present in the list")
else:
    print("apple is not present in the list")



# ---------------length of list-------------------
mylist6 = ["apple", "mango", "kiwi", "orange", "melon", "mango"]
print(len(mylist6))



# -------------------adding items-------------------
# append add in the last
mylist6 = ["apple", "mango", "kiwi", "orange", "melon", "mango"]
mylist6.append("new List")
print(mylist6)

#insert------index and value
mylist6 = ["apple", "mango", "kiwi", "orange", "melon", "mango"]
mylist6.insert(2,"new list")
print(mylist6)


# -----------remove elements...............
#pop
l1 = [12,3,4,56,78,54,23]
l1.pop(3)
print(l1)   #56 at index 3 will be remove

#remove
l1 = [12,3,4,56,78,54,23]
l1.remove(78)
print(l1)   #78 will be remove

#del
l1 = [12,3,4,56,78,54,23]
del l1[0]
print(l1)   #12 will be remove

#clear
l1 = [12,3,4,56,78,54,23]
l1.clear()
print(l1)   #empty the list


# ----------------------------COPY A LIST----------------------
l1 = [12,34,56]
l2 =list(l1)    #1st method
l3 = l1.copy()      #2nd method
print(l1)
print(l2)
print(l3)

#......................joining two list................................
l1 = [12,34,56]
l2 = [89,54,32]
s = l1+l2
print(s)

#------------------combine two list-------------------------------------
l1 = ["a", "b", "c"]
l2 = ["i", "j", "k"]
for item in l2:
    l1.append(item)
print(l1)

#..........................
l1 = ["a","b","c"]
l2 = ["i","j","k"]
l1.extend(l2)
print(l1)


#-------------Reading a list of number from user input........................
# a = input("Enter the list: ").split(",")        #string
# print(a)

# b = tuple(map(int,(input("Enter the element of tuple :").split(","))))
# print(b)

#for integer type---------------------------------------------------
# b = list(map(int,(input("Enter the element of list :").split(","))))
# print(b)

#for float type---------------------------------------------------
# b = list(map(float,(input("Enter the element of list :").split(","))))
# print(b)


#-------------------------sorting a list------------
mylist = [12, 9, 4, 67]
mylist.sort()
print(mylist)


#..............................reverse a list...........
mylist = [12, 9, 4, 67]
mylist.sort(reverse = True)
print(mylist)

#---------------------count------------
mylist = [12, 9, 4, 67,12,12,12,12]
print(mylist.count(12))


