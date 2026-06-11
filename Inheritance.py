# Inheritance = creating a new class based on an existing class

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    # Dog inherits everything from Animal
    pass


dog = Dog()
dog.speak()