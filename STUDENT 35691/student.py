class Student:
    def __init__(self, name, grade, index_number):
        self.name = name
        self.grade = grade
        self.index_number = index_number

s1 = Student("Anna", "A", "12345")

print(s1.name)
print(s1.grade)
print(s1.index_number)