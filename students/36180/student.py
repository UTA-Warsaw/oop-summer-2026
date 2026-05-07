class Student:
    def __init__(self, name, grade, index_number):
        self.name = name
        self.grade = grade
        self.index_number = index_number

    def __str__(self):
        return f"Student: {self.name}, grade : {self.grade}, index number: {self.index_number}"

s1 = Student("Anna", "A", "36180")
print(s1)  
print(s1.grade)