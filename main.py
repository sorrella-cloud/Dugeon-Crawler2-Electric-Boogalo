#Dungeon Crawler 2: Electric Boogaloo the Remix, Reloaded
#Anthony Sorrell Final Project 3/15/26
#Game main and level flow, class selection, room traversal, and random events
#monsters, loot, shops, with end-of-dungeon summary. Uses player_combat to #import classes to pick from and combat turn based mechanic
#and monster modules for various monster child classes.
#resources
#GitHub search for dungeon crawlers made with python
#https://github.com/topics/dungeon-crawler?l=python&o=desc&s=updated&utm_source=copilot.com
#deepest dungeon walkthrough
#https://damom73.github.io/python-oop-with-deepest-dungeon/?utm_source=copilot.com



import random
from monster import Skeleton, GoblinHorde, DeathKnight, Rat
from player_combat import Fighter, Magus, Rogue, combat




#character selection prompt that creates an instace of fighter magus or rogue class with basic error handling
def choose_class():
    print("Choose your class:")
    print("1. Fighter")
    print("2. Magus")
    print("3. Rogue")

    choice = input("Enter a number between 1 and 3: ").strip()

    if choice == "1":
        return Fighter()
    elif choice == "2":
        return Magus()
    elif choice == "3":
        return Rogue()
    else:
        print("Invalid choice, please try again..........")
        return choose_class()

#precombat where you can use potions or Aelixir if you have them
def pre_combat_use(player, inventory):
    if not inventory:
        return

    print("Do you want to use an item before combat?")
    print("1. Use Potion")
    print("2. Use AElixir")
    print("3. No")

    choice = input("> ").strip()

    if choice == "1" and "potion" in inventory:
        if player.health < 20:
            player.health += 10
            inventory.remove("potion")
            print("You used a Potion!")
        else:
            print("Health already full!")

    elif choice == "2" and "AElixir" in inventory:
        if player.magii < 20:
            player.magii += 10
            inventory.remove("AElixir")
            print("You used an AElixir!")
        else:
            print("Magii already full!")

#returns a random monster from the list
def random_monster():
    monsters = [Skeleton, GoblinHorde, DeathKnight, Rat]
    return random.choice(monsters)()

#shop function that removes gold and add item purchase from shop to players inventory
def shop(player):
    while True:
        print("You find a small shop in the dungeon!")
        print("Choose to buy something or continue on!")
        print("1. Buy Potion (5 gold)")
        print("2. Buy AElixir (7 gold)")
        print("3. Leave")
        print(f"You have this much gold: {player.gold}.")

        choice = input(": ").strip()

        if choice == "1":
            if player.gold >= 5:
                player.gold -= 5
                print("You bought a Potion!")
                print("Use this to replenish health")
                return "potion"
            else:
                print("Not enough gold to buy a Potion.")

        elif choice == "2":
            if player.gold >= 7:
                player.gold -= 7
                print("You bought an AElixir!")
                print("Use this to replenish magii")
                return "elixir"
            else:
                print("Not enough gold to buy an AElixir.")

        elif choice == "3":
            print("You leave the shop.")
            return None

        else:
            print("You have to pick a valid choice...")


#Main game loop which intros players to games handles events and displays final status once a round is done
def main():
    print("Welcome to Dungeon Crawlers 2: Electric Boogaloo, the Remix, Reloaded.")
    print("In this game you will choose a class, enter a dangerous dungeon, fight monsters, maybe find loot.")
    print("You can leave the dungeon after battle or continue on to glory")
    print("If you do choose to venture on heal yourself if possible")
    print("Also if playing mage remember to replenish magii Magus does not use attack stats")
    print("You notice a sign as you approach----")
    print("NOTICE: Villagers and Scouts have reported deadly Deathknight")
    print("PROCEED WITH CAUTION!!!!!")
    player = choose_class()
    print(f"You have chosen: {player.name}")

    rooms = ["Entrance", "Hallway", "Chamber", "Crypt", "Treasure Room"]
    inventory = []

    game_run = True
    room_index = 0

    while game_run and room_index < len(rooms):
        room = rooms[room_index]
        if room == "Entrance":
            print(f"You enter the {room} This is the start of your journey!")
        else:
            print(f"You enter the {room} and")

        event = random.choice(["monster", "loot", "empty", "shop"])

        if event == "shop":
            item = shop(player)
            if item:
                inventory.append(item)

        elif event == "monster":
            pre_combat_use(player, inventory)
            m = random_monster()
            result = combat(player, m)
            if not result:
                game_run = False

        elif event == "loot":
            print("You found some gold!")
            player.gold += random.randint(1, 5)

        else:
            print("The room is empty.")


        if game_run and player.health > 0:
            leave = input("Do you want to leave the dungeon now? (y)es/(n)o: ").strip().lower()
            if leave == "y":
                print("You leave the dungeon and head back to safety.")
                print("Whether a coward or a decisive choice...")
                print("you live to fight another day")
                game_run = False

        room_index += 1

    print("---------------------------------------------------------------------------------------")
    if player.health <= 0:
        print("Game Over! A Monster killed you while venturing and since")
        print("and since you ventured alone no one ever heard what happened or saw you ever again.")
    elif not game_run:
        print("You left the dungeon and survived.")
        print("You live to fight another day.")
    else:
        print("You explored the dungeon to the end and survived the expedition!")
        print("You Arise a Hero.")

    player.display()


if __name__ == "__main__":
    main()
