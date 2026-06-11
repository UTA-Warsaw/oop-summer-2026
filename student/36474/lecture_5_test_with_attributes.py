# Hsuh: creating a class with object attributes (first_name, last_name)
class Person:
    def __init__(self, first_name, last_name):
        # Hsuh: storing first and last name for each object
        self.first_name = first_name
        self.last_name = last_name

# Hsuh: creating an object of Person
person1 = Person("John", "Doe")  # ✅ обе строки закрыты кавычками и скобками

# Hsuh: printing the object's attributes
print(person1.first_name)  # John
print(person1.last_name)   # Doe

