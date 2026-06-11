class Animal:
    def make_sound(self):
        print("Generic sound")

class Cat(Animal):
    def meow(self):
        print("Meow!")

my_cat = Cat()
my_cat.make_sound()
my_cat.meow()