class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Anna", "A")

print(s1.grade)

s1.grade = "B"

print(s1.grade)
