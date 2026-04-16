class Student:
  def __init__(self, name, grade, index_number):
    self.name = name
    self.grade = grade
    self.index_number = index_number

# Create an object
s1 = Student("David", "B" , 36492)

# Print the grade
print(s1.grade)

# Change the grade
s1 = "A"

# Print the updated grade
print(s1.grade)

# Print the idex number
print(s1.index_number)
