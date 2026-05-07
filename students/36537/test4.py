class Shape:
    def __init__(self, side_a):
        self.side_a = side_a

class Square(Shape):
    def __init__(self, side_a):
        super().__init__(side_a)
    def calc_area(self):
        self.area = self.side_a**2
        return self.area

class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        super().__init__(side_a)
        self.side_b = side_b
    def calc_area(self):
        self.area = self.side_a*self.side_b
        return self.area


s1 = Square(4)
r1 = Rectangle(5, 6)
print(s1.calc_area())
print(r1.calc_area())