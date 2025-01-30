# {}
# unordered collections - does not support indexing

my_set = {1,2,4}
print(my_set)


print("# ---------------unique elements-------------")
# does not allow duplicate elements

my_set = {1,1,2,2,3,3,4,4,5}
print(my_set)       #{1,2,3,4,5}



print("# -------------mutable(but not elements................")
my_set = {1,2,3}
my_set.add(4)
print(my_set)

my_set.remove(2)
print(my_set)



print("# --------Allowed elements-----------")
my_set = {1,"hello",(1,4)}
print(my_set)
# my_set - {1,"hello",[1,4]}  #elements are immutable ----TypeError: unhashable type: 'list'



print("# ----------creating sets--------------------")
my_set = {"mango","cherry","Banana"}
print(my_set)

print("#----------------add one items in sets--------------------------")
# add-we can add only one items
#update-we can add multiple items

my_set = {"One", "Two","Three"}
my_set.add("Four")
print(my_set)
print("#----------------add multiple items in sets--------------------------")
set1 = {"five","six"}
my_set.update(set1)
print(my_set)

print(len(my_set))

print("#---------------remove elements from the set--------------------")
# remove
set1 = {"five","six","seven","eight"}
set1.remove("five")
print(set1)

# set1.remove("ten")
# print(set1)

# discard
set1 = {"five","six","seven","eight"}
set1.discard("five")
print(set1)

# set1.discard("ten")
# print(set1)

# The difference is if items is not present in list and we try remove or discard then remove will show error and discard will not show any error


print("-----------Union of two sets--------------")
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 | set2)
print(set1.union(set2))



print("----------------Intersection----------------------")
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 & set2)
print(set1.intersection(set2))

print("-------------------difference-------------")
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 - set2)
# print(set2 - set1)
print(set1.difference(set2))


print("----------------------Symmetric difference----------------")
set1 = {1,2,3,4}
set2 = {1,5,3}
print(set1 ^ set2)           #common elements will not printed



print("---------------------------frozenset---------------------")
# immutable version of sets,once created cant modify
frozenset1 = frozenset([1,2,3])
print(frozenset1)

# frozenset1.add(15)   #we cant add or remove
# print(frozenset1)     #Attribute error



print("-------------------------List conversion into sets--------duplicate handling--------------")
mylist = [1,2,3,3,4,4]
my_set = set(mylist)        #set
print(my_set)



