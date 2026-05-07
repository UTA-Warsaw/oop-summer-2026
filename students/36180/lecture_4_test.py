from datetime import datetime

my_favorite_food = "kebab"

class Car: 
    def __init__ (self ,brand,size):
        self.brand = brand
        self.size = size  
        self.isworking = False 
        self.creation_time = datetime.now()

c1 = Car("mercedes","5")

print("created date",c1.creation_time)

MIN_PASSWORD_LENGTH = 8

#this is comment line 
# x = [1,2,3]
