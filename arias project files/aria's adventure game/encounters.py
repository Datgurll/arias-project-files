
import random
from characters import Player

def encounter_monster_with_story(player, monsters):
    monster = random.choice(monsters)
    print(f"A wild {monster.name} appears! It is level {monster.level}.")

    dialogue_choice = input("What would you like to do? (1: Fight, 2: Run, 3: Talk): ")

    backstory = {
        "Goblin": "The goblin was stealing food for its hungry family.",
        "Zombie": "The zombie was once a brave knight, cursed into this form.",
        "Zombie Dog": "This poor dog was transformed by a dark spell.",
        "Orc": "The orc is a warrior exiled from its tribe, searching for redemption.",
        "Dragon": "The dragon is an ancient guardian of the forest's magic."
    }

    if dialogue_choice == '1':
        handle_fight(player, monster)
    elif dialogue_choice == '2':
        handle_run(player, monster)
    elif dialogue_choice == '3':
        handle_talk(player, monster, backstory)

def handle_fight(player, monster):
    print("You chose to fight!")
    if player.level >= monster.level:
        print("You defeated the monster!")
        player.experience += 10
        player.gold += 5
        print(f"You gained 10 experience and 5 gold. Current EXP: {player.experience}, Gold: {player.gold}.")
        if player.level == 2 and player.special_ability:
            print(f"You used your special ability: {player.special_ability}")
    else:
        print("The monster is too strong! You take 10 damage.")
        player.health -= 10
        print(f"Current Health: {player.health}")

def handle_run(player, monster):
    print("You chose to run away!")
    escape_chance = random.randint(1, 10)
    if escape_chance > 3:
        print("You successfully escaped.")
    else:
        print("You failed to escape and took 5 damage.")
        player.health -= 5
        print(f"Current Health: {player.health}")

def handle_talk(player, monster, backstory):
    print("You attempt to talk to the monster.")
    talk_chance = random.randint(1, 10)
    if talk_chance > 3:
        print("You successfully talked the monster down.")
        print(f"Monster's Backstory: {backstory.get(monster.name, 'Unknown')}")
    else:
        print("The monster attacked you anyway! You took 5 damage.")
        player.health -= 5
        print(f"Current Health: {player.health}")
