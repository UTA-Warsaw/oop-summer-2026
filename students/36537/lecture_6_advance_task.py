class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(self.name, 'says: ...')
    
class Cat(Animal):
    def __init__(self, name, age, jump_height):
        super().__init__(name, age)
        self.jump_height = jump_height
    def say(self):
        print(self.name, "says: Meow!")

class Lizard(Animal):
    def __init__(self, name, age, tongue_lenght):
        super().__init__(name, age)
        self.tongue_lenght = tongue_lenght

c1 = Cat('Barsik', 3, 120)

l1 = Lizard('Jack', 1, 10)
c1.say()
l1.say()


