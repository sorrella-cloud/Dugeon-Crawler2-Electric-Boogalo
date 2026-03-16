#Base item and child classes used by the game, Potion, AElixir, and GoldCoin.
#Each item stores stats like health, magii, amount and provides a small
#use method for items.




#base item class used for item objects
class Items:
    def __init__(self, name, health, magii, amount):
        self.name = name
        self.health = health
        self.magii = magii
        self.amount = amount

    def display(self):
        print(self.name)
        print(self.health)
        print(self.magii)
        print(self.amount)

#potion for health
class Potion(Items):
    def __init__(self):
        super().__init__("Potion", 10, 0, 1)

    def use(self, player):
        player.health += 10
        print("The Potion healed you for 10 health!")

#Aelixir for magii
class AElixir(Items):
    def __init__(self):
        super().__init__("AElixir", 0, 10, 1)

    def use(self, player):
        player.magii += 10
        print("Your magii increased by 10!")

#place to track gold
class GoldCoin(Items):
    def __init__(self, amount=1):
        super().__init__("Gold Coin", 0, 0, amount)
