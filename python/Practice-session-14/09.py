# Create a module math operations.py with function add, sub, mul and div. Write a script to omplement and use these functions.

class math_operation:
    def add(self,a,b):
        print(f"sum is : {a+b}")
    def sub(self,a,b):
        print(f"Subtraction is: {a-b}")
    def mul(self,a,b):
        print(f"Multiplication is: {a*b}")
    def div(self,a,b):
        print(f"Division is: {a/b}")
ob1 = math_operation()
ob1.add(10,20)
ob1.sub(20,10)
ob1.mul(10,20)
ob1.div(20,10)