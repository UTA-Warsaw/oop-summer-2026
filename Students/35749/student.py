class Student:
    def __init__(self, name, grade, indexnum):
        self.name = name
        self.grade = grade
        self.indexnum = indexnum

s1 = Student("Anna", "A", "12345")

print(s1.grade)
print(s1.indexnum)
s1.grade = "B"
s1.indexnum = "23456"
print(f"Her grade is changed to {s1.grade}")
print(f"Her new index number is {s1.indexnum}")