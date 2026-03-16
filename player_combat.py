#Player classes and combat logic. Defines a Player base class and three player
#types, Fighter, Magus, and Rogue with  special skills. The combat
#function turn-based and fight between a player and a monster grants gold depending on monster.

import random
from monster import reward


#base class for player stats.
class Player:
    def __init__(self, name, attack, health, magii, gold):
        self.name = name
        self.attack = attack
        self.health = health
        self.magii = magii
        self.gold = gold
        self.special = None

    def display(self):
        print("Character Name:", self.name)
        print("Attack:", self.attack)
        print("Health:", self.health)
        print("Magii:", self.magii)
        print("Gold:", self.gold)
        print("Special:", self.special)
        print()


    def Speciality(self):
        return False

#fighter class with higher attack and experience buff when entering combat and receives injury.
class Fighter(Player):
    def __init__(self):
        super().__init__("Fighter", 15, 20, 0, 10)

    def Speciality(self):
        if self.health < 20:
            self.attack = 20
            self.special = "Experienced"
        return False

#magic class focusing on high damage but squishy, uses magii instead of attack and gets magic buff when health is low.
class Magus(Player):
    def __init__(self):
        super().__init__("Magus", 0, 10, 20, 15)

    def Speciality(self):
        if self.health < 10:
            self.magii = 30
            self.special = "Innate Magic"
        return False

#rogue thief that can easily dodge attacks randomly
class Rogue(Player):
    def __init__(self):
        super().__init__("Rogue", 25, 7, 0, 25)

    def Speciality(self):
        if self.health < 10:
            if random.random() < 0.5:
                self.special = "Assassin Step"
                return True
        return False

#main combat loop for players fighting monsters using turn based combat
#and bool values to check with while loop if player or monster died and specials
def combat(player, monster):
    turn = 1
    print(f"A {monster.name} appears!")

    alive = True

    while alive and monster.defense > 0:
        print(f"--- Turn {turn} ---")

        special_active = player.Speciality()

        damage = player.attack if player.magii == 0 else player.magii
        monster.defense -= damage
        print(f"You hit the {monster.name} for {damage} damage!")

        if monster.defense > 0 and hasattr(monster, "specialSkill"):
            try:
                monster.specialSkill(turn)
            except TypeError:
                monster.specialSkill()

        if monster.defense > 0:
            dodged = isinstance(player, Rogue) and bool(special_active)
            if dodged:
                print("You dodged the attack!")
            else:
                player.health -= monster.attack
                print(f"The {monster.name} hits you for {monster.attack} damage!")

        if player.health <= 0:
            alive = False

        turn += 1

    if not alive:
        print("You died!")
        return False
#give gold upon victory
    print(f"You defeated the {monster.name}!")
    loot = reward(monster)
    player.gold += loot.amount
    print(f"You gained {loot.amount} gold!")

    return True
