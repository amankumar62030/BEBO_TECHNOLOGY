# Access specifier define the scope of varible class and method

# types
# 1.public      a
# 2.private  __a
# 3.protected  _a


#private variable
class PrivateExample:
    def __init__(self):
        self.__private_var = "I am a private variable"

    def __access_private(self):
        print(self.__private_var)

    def display(self):
        self.__access_private()


obj = PrivateExample()
# obj._PrivateExample__access_private()
obj.display()



#public example
class PublicExample:
    def __init__(self):
        self.public_var = "I am a public variable"
    def access_public(self):
        print(self.public_var)

ob1 = PublicExample()
ob1.access_public()





#protected example
class ProtectedExample:
    def __init__(self):
        self._protected_var = "I am a protected variable"
    def access_protected(self):
        print(self._protected_var)
ob1 = ProtectedExample()
ob1.access_protected()

