# Create the Student class
class Student:
    def __init__(self, name, grade, index):
        self.name = name
        self.grade = grade
        self.index = index

# Create an object
s1 = Student("Anna", "A", 12345)

# Print the grade
print(s1.grade)

# Change the grade
s1.grade = "B"

# Print the updated grade
print(s1.grade)

# Print the index number
print(s1.index)
