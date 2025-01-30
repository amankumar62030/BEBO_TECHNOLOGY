# create a package utilities with string_util.py(with functions like reverse_string and is_palindrome) and number_util.py(with functions like is_even and is_prime). use these utilites in python script.

class sTr:
    def reverse_string(self,str):
        rev=""
        self.str = str
        for i in str:
            rev = i+rev
        print(f"{rev}")

    def is_palindrome(self,str1):
        rev = ""
        self.str1 = str
        for i in str1:
            rev = i + rev
        if(str1==rev):
            print("Palindrome")
        else:
            print("Not Palindrome")
ob1 = sTr()
ob1.reverse_string("aman")
ob2.is_palindrome("aman")

