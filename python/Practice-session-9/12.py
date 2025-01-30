# 12.	Create a function that calculates the simple interest given the principal, rate of interest, and time. Use default values for the rate of interest and time

def simple_Interest(p, r=2, t=3):
    si = p * r * t / 100
    return si

p = int(input("Enter Principal: "))

print(f"Simple Interest is: {simple_Interest(p)}")
