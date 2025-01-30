# 10.	Write a program to calculate the final price of an item .

def calculate_final_price():
    price1 = float(input("Enter the price of item 1: "))
    price2 = float(input("Enter the price of item 2: "))
    price3 = float(input("Enter the price of item 3 (or 0 if none): "))

    total_price = price1 + price2 + price3
    print(f"The total price of the items is: ₹{total_price:.2f}")

calculate_final_price()
