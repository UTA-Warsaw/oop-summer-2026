class ClassWithAttributes:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

person_obj = ClassWithAttributes("Dmitry", "Simonov")

print(f"First name: {person_obj.first_name}")
print(f"Last name: {person_obj.last_name}")