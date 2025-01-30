# 14.	Implement a nested function that demonstrates how inner functions can access variables from the outer function.

def outer_func(outer_var):
    print("Outer function",outer_var)

    def inner_func(inner_var):
        print("Inner function",inner_var)

        print("Calling outer inside inner:",outer_var)
    inner_func(4)
outer_func(45)

