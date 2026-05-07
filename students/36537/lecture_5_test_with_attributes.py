class Table:
    def __init__(self, numlegs, color):
        self.numlegs = numlegs
        self.color = color

t1 = Table(4, 'black')

print(t1.numlegs, t1.color)