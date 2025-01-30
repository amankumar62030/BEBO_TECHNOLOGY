# Create a class ShoppingCart to add, remove and display items.

class ShoppingCart:

    def __init__(self,name):
        self.name = name
        self.shopping_items = 0.0

    def add_items(self,add):
        if add > 0:
            self.shopping_items+=add

    def remove_items(self,remove):
        if remove < self.shopping_items:
            self.shopping_items-=remove
        else:
            print("Insufficient items")
    def display_items(self):
        print(self.shopping_items)

        def display_items(self):
            print(f"Items in {self.name}: {self.shopping_items}")

ob1 = ShoppingCart("Toy Cart")
ob1.display_items()
ob1.add_items(50)
ob1.remove_items(10)
ob1.display_items()


