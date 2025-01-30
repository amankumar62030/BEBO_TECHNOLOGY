# Write a product class with instance attribute for name and price. Add a class method set_discount(add_items,discount) to apply a discount to all products. Use this class method to change the price of all created products.


class Product():
    ProductList=dict({'phone':100,'tv':120,'watch':80})
    def set_discount(self,dis):
        # self.dis=dis
        for key,value in Product.ProductList.items():
            temp=( (value * dis)/100)
            Product.ProductList[key]=temp
    def display(self):
        for i,j in Product.ProductList.items():
            print(i,j,end=" ")
ob=Product()
ob.set_discount(10)
ob.display()