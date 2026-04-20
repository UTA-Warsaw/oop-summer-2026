class Laptop:
    def __init__(self,brand,year,price,ram):
        self.brand=brand
        self.year=year
        self.price=price
        self.ram=ram

    def info(self):
        print(f"The laptop is of year{self.year} ,from year{self.year}and RAM {self.ram}G,at retail price {self.price}zl")

laptop1=Laptop("Philips",2005,373,15)
laptop2=Laptop("Delhi",2023,39229,100)
print(laptop1.info())
print(laptop2.info())