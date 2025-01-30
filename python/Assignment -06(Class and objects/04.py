# 4.	Write a Product class with instance attributes for name and price. Add a class method set_discount(cls, discount) to apply a discount to all products.
# Use this class method to change the price of all created products.

class Product:
    discount = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def set_discount(cls, discount):
        cls.discount = discount

    def get_discounted_price(self):
        return self.price * (1 - self.discount / 100)

# Example usage
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)

print("Original Prices:")
print(f"{product1.name}: {product1.price}")
print(f"{product2.name}: {product2.price}")

# Apply a discount
Product.set_discount(10)

print("\nPrices After 10% Discount:")
print(f"{product1.name}: {product1.get_discounted_price()}")
print(f"{product2.name}: {product2.get_discounted_price()}")
