class Student:
  def __init__(self, name, grade, index_number):
    self.name = name
    self.grade = grade
    self.index_number = index_number
s1 = Student("Enes", "A" , 12345)
print(s1.grade)
s1.grade = "B"
print(s1.grade)