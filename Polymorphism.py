# Polymorphism = same method name, different behavior

class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


# same method name, different output
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()