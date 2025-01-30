# Wrapping up of data


class Student:
    def __init__(self, name, age):
        self.__name = name  # private scott
        self.__age = age  # private

    # getter for name
    @property
    def name(self):
        return self.__name

    # setter for name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # getter for age

    @property
    def age(self):
        return self.__age

    # setter for age
    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("invalid age")


s = Student("Bob", 22)
print(s.name)
print(s.age)

s.name = "Satwinder"
s.age = 34
print(s.name)
print(s.age)