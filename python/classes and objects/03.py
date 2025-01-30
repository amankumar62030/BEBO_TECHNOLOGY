class myclass:
    a, b = 10, 20

    def add(self,a, b):
        print(a + b)

    def multiply(self):
        print(self.a + self.b)

    # def method2():
    def notstatic():
        print("not static")

    @staticmethod
    def method1():
        print("Static")


# obj1 = myclass()
# obj1.add()
myclass.method1()
myclass.notstatic()
myclass.add(0,10, 20)