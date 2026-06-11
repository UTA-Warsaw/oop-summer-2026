# --- POLYMORPHISM EXAMPLE ---

class Dog:
    def make_sound(self):
        print("The dog barks: Woof Woof!")

class Cat:
    def make_sound(self):
        print("The cat meows: Meow Meow!")

# A common function that handles different object types
def animal_sound_trigger(animal_object):
    animal_object.make_sound()

# --- TESTING POLYMORPHISM ---
if __name__ == "__main__":
    doggy = Dog()
    kitty = Cat()

    # Same function call, different behaviors
    animal_sound_trigger(doggy) # Output: The dog barks: Woof Woof!
    animal_sound_trigger(kitty) # Output: The cat meows: Meow Meow!