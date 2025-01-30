# WAP that convert a tuple of number to a list, appends a given number to a list, and then convert it back to tuple.


t1 = (10,20,30,40,50)

t2 = list(t1)
t2.append(60)
t3 = tuple(t2)
print(t3)
