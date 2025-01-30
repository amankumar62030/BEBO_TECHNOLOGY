# Error
# types---------
# syntax---------compiler
# logical
# run-time--------occurs at the execution of the code


# Example-01
# print("This is starting of the program")
# print("This is starting of the program")
# print("This is starting of the program")
# print("This is starting of the program")
# print(10/0) #-------exception handle---successful termination
# print("This is end of the program")
# print("This is end of the program")
# print("This is end of the program")
# print("This is end of the program")




#To avoid termination, we need to handle the exception..........
# To handle the exception we have try, except, else, finally
# try: code that might cause the exception
# except: / expect someExceptionName as e: code to handle the exception
# else: code to execute if no exception occured
# finally: code that will run no matter what


# Example----------02
# print("This is starting of the program")
# print("This is starting of the program")
# print("This is starting of the program")
# print("This is starting of the program")
# try:
#     print(10/5)
#     print(10/0)
# # except:
# #     print("The exception occured in the code")
# except Exception as e:
#     print(e)
# finally:
#     print("Done")
# print("This is end of the program")
# print("This is end of the program")
# print("This is end of the program")



# Example---03--------------
# Multiple except block try,except,ekse,finally

# num1,num2 = 10,0
# try:
#     result = num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("Throw ZeroDivisionError Exception")
# except FileNotFoundError:
#     print("File not found exception")
# except SyntaxError:
#     print("Syntax error exception")
# except Exception as e:
#     print(e)
# else:
#     print("No Exception occured")
# finally:
#     print("Always Execute")


# Example---04(Rising our own exception)
# def enterage(num):
#     if num < 0:
#         raise ValueError()      #this will throw exception
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
#
# num = -1
# try:
#     enterage(num)
# except ValueError:
#     print("THis is exception in code")
#
# print("Program terminated")


# Example--05 Custom Exception--we can define custom exception by creating a class

#Syntax:
# class customError(Exception):
#     pass
# try:
#     raise customError("This is a custom error message")
# except customError as e:
#     print(e)


class NegativeNumberException(Exception):
    def __init__(self,msg = "Negative values are not allowed"):
        self.msg = msg
        super().__init__(self.msg)
# function to check the number is positive or negative number

def check_positive(number):
    if number<0:
        raise NegativeNumberException()
    else:
        print(f"The number {number} is positive")
try:
    num = int(input("Enter the number: "))
    check_positive(num)
except NegativeNumberException as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)