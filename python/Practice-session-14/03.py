# Write a Counter class with a class variable count to keep trak of how many objects have been created.Test this by creating multiple objects and printing the count

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    def display_info(self):
        print(f"Total number of object created is: {Counter.count}")

ob1 = Counter()
ob2 = Counter()
ob3 = Counter()
ob4 = Counter()
ob5 = Counter()
ob3.display_info()


