class Rectangle:
    def __init__(self,width,height,perimetr):
        self.width = width
        self.height = height
        self.perimetr = perimetr

    def area(self):
      return self.width * self.height
    def perimetr(self):
      return self.width * self.height
    
r1 = Rectangle(4,5)
print(r1.area())



