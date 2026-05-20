class Car:
    def __init__(self,speed,hp):
        self.speed = speed
        self.hp = hp
    def move(self):
        print("Driving")
class Bike:
    def __init__(self,speed,hp):
        self.speed = speed
        self.hp = hp
    def move(self):
        print("Riding")
car1 = Car(312,890)
bike1 = Bike(312,180)
for x in(car1,bike1):
    x.move()