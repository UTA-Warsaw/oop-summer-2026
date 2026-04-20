class Student:
    def __init__(self,name,grade,index_number):
        self.name=name
        self.grade=grade
        self.index_number=index_number
s1=Student("Anna","A",356173)
s1.grade="B"
print(s1.grade)