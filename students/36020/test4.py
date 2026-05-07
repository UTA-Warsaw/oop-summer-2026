#Create classes for square and rectangle thre should be a paren class for them 
class GeoFigure:
    def __init__(self, side_a):
        self.lenght = side_a
    def all_info(self):
        print(f"lengt of one side is {self.lenght}cm, Perimeter is {self.lenght * 4} and the area is {self.lenght * self.lenght}")
class Square(GeoFigure):
    pass
    
    

class Rectangle(GeoFigure):
    def __init__(self, side_a, side_b):
        super().__init__(side_a)
        self.height = side_b
    
    def all_info(self):
        print(f"lengt of one side is {self.lenght}cm,heigt is{self.height} Perimeter is {self.lenght * 2 + self.height * 2} and the area is {self.lenght * self.lenght}")

sq1 = Square(5)
rec1 = Rectangle(5,4)
rec1.all_info()
sq1.all_info()

