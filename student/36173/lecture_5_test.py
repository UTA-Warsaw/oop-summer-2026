#a)
# 
# 
# 
# #creating class and objects 
class Chair:
    wheels = 4

    def __init__(self,location,colour,year):
        self.location=location 
        self.colour =colour
        self.year = year 
    def description(self):
        return f"at {self.location} the chair is {self.colour} ,it was made in {self.year}"
chair1=Chair("desk 1","blue",2025)
chair2=Chair("desk 2","black",2024)
chair4=Chair("desk3","red",2022)
print(chair1.description())
print(chair2.colour)
print(chair4.description())
print(chair4.wheels)

class Country:
    pass 
class Students:
    year = "2025/2026"
    def __init__(self,student_id)