#tuples are immutable

t = (1,23,45,67,45.6)
print(t)
# t[0] = 200
# print(t)


name = (1,23, "Rohan", True, 45.6,23,23)
print(name.count(23))   #it will return no. of times 23 occurs

print(name.index("Rohan"))


#--------------concatination----------------------
t1 = (12,13,14)
t2 = (15,16,17)
con = t1+t2
print(con)      #(12, 13, 14, 15, 16, 17)
print(len(con)) #6

print(sum(t1))  #39

print(2 in t1)   #false
print(2 not in t1)   #true
print(12 in t1) #true


print(min(t1))   #12
print(max(t2))  #17


print(t1.index(13))   #1


s = (12,54,10,9)
print(sorted(s))        #[9, 10, 12, 54]

# s = (12,54,10,9)
# print(pop(3))       ## This will raise a NameError

s = (12,54,10,9)
del s
print(s)