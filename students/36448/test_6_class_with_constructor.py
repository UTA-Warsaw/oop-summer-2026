class Monitor:
    def __init__(self, brand, size, color, shape):
        self.brand = brand
        self.size = size
        self.color = color
        self.shape = shape
m1 = Monitor("philips", 23, "black", "flat")
             
print(m1.brand, m1.size, m1.color, m1.shape)