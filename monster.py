#Defines Monster base class and  monsters ,Skeleton, GoblinHorde,
#DeathKnight, and Rat. Each monster has attack, defense, and a special skill.
##Also provides a reward function that returns GoldCoin  for which monster you killed.




from economy import GoldCoin


#base monster class
class Monster:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.special = None

    def display(self):
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Special:", self.special)
        print("Name:", self.name)
        print()

#skeleton class with special that activates under low health
class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", 5, 10)

    def specialSkill(self):
        if 1 <= self.defense <= 5:
            self.defense = 15
            self.special = "Regenerate"

#golblin group class that gets a buff once health drops
class GoblinHorde(Monster):
    def __init__(self):
        super().__init__("Goblin Horde", 3, 15)

    def specialSkill(self):
        if self.defense <= 7:
            self.attack = 10
            self.special = "Outnumbered"

#boss fight that usually kills players with alternating special depending on turn
class DeathKnight(Monster):
    def __init__(self):
        super().__init__("Death Knight", 15, 40)

    def specialSkill(self, turn):
        if turn % 2 == 0:
            self.attack = 30
            self.special = "Unholy Power"

#weak creature that can get big if left unchecked
class Rat(Monster):
    def __init__(self):
        super().__init__("Rat", 1, 3)

    def specialSkill(self):
        if self.defense <= 2:
            self.attack = 4
            self.special = "Rabidness"

#function to track gold per monster
def reward(monster):
    if monster.name == "Skeleton":
        return GoldCoin(3)
    elif monster.name == "Goblin Horde":
        return GoldCoin(2)
    elif monster.name == "Death Knight":
        return GoldCoin(25)
    elif monster.name == "Rat":
        return GoldCoin(1)
