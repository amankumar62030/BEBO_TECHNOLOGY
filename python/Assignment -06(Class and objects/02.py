# 2.	Write a Counter class with a class variable count to keep track of how many objects have been created. Test this by creating multiple objects and printing the count.



class Counter:
    count = 0
    def __init__(self):
        Counter.count+=1

ob1 = Counter()
ob2 = Counter()
ob3 = Counter()
ob4 = Counter()
print(Counter.count)
