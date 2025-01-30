# Create a class Counter with a class variable count that keep track of the number of objects created. Increment count each time an object is created and display the total number of object created.

class Counter:
    count = 0

    def m1(self):
        Counter.count += 1      #class variable(static)
        print(self.count)
        # print(Counter.count)


obj1 = Counter()
obj1.m1()
obj2 = Counter()
obj2.m1()
obj3 = Counter()
obj3.m1()

