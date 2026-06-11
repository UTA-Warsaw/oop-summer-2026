class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def show_health(self):
        return self.__health


hero = GameCharacter("Knight", 100)
hero.take_damage(35)
print(hero.name, hero.show_health())