class Player:
    def __init__(self, name, hp, atk, lvl):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.lvl = lvl
p1 = Player("PLAYER1", 255, "45", "15")
             
print(p1.name, p1.hp, p1.atk, p1.lvl)

class Enemy:
    def __init__(self, name, hp, atk, lvl):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.lvl = lvl
e1 = Enemy("goblin", 100, 25, 5)
print(e1.name, e1.hp, e1.atk, e1.lvl)