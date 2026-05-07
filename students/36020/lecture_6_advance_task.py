class Enemy:
    def __init__(self, creature):
        self.creature = creature
    def attack(self):
        print (f"{self.creature} Hit you with huge bat")

class Ogre(Enemy):
    pass

class Goblin(Enemy):
    def attack(self):
        print (f"{self.creature} hexed you into a chicken")

class Dragon(Enemy):
    def attack(self):
        print (f"{self.creature} casted fireball")

ogr1 = Ogre("Green Ogre")
gob1 = Goblin("Goblin shaman")
drag1 = Dragon("Red Dragon")
for i in (ogr1, gob1, drag1):
    i.attack()
