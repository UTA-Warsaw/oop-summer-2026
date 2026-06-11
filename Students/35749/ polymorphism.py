class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.speak())