class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r1 = Rectangle(5, 3)
print(f"Area: {r1.area()}")
print(f"Perimeter: {r1.perimeter()}")