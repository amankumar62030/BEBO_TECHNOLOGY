# Implement a class Product with private attributes price and stock.Use getter and setter methods to ensure the price and stock values
# cannot be negative.


class Product:
    def __init__(self,price,stock):
        self.__price = price
        self.__stock = stock

    #getter for price
    @property
    def price(self):
        return self.__price

    #setter for stock
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invaild")

    #getter for stock
    @property
    def stock(self):
        return self.__stock

    #setter for stock
    @stock.setter
    def stock(self,new_stock):
        if new_stock > 0:
            self.__stock = new_stock
        else:
            print("Invalid")
c = Product(20000,12)
print(c.price)
print(c.stock)

c.price = 0
c.stock = 0

