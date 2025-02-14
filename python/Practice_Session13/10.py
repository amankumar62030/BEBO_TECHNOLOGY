# 10.	Create a class ShoppingCart to add, remove, and display items.

class ShoppingCart:
    def __init__(self):
        self.cart = []  # List to store items

    def add_item(self, item):
        self.cart.append(item)
        print(f"{item} added to cart.")

    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")

    def display_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("Shopping Cart:", self.cart)

# Example Usage:
cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.display_cart()
cart.remove_item("Apple")
cart.display_cart()
