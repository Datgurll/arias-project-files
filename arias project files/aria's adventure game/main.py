# Updated full game code with character backstories and enhanced story elements

# Function to create a new player with backstory
def create_player_with_backstory(weapon_choice):
    player_class = weapon_to_class[weapon_choice]
    attrs = initial_attributes[player_class]
    player = Player(player_class, weapon_choice, attrs["health"], attrs["experience"], attrs["gold"], attrs["level"])
    player.backstory = character_backstories[player_class]
    return player

# Function to show the player's initial stats and backstory
def show_initial_stats_and_backstory(player):
    print(f"\nCongratulations, you are a {player.player_class}!")
    print("Your initial stats are:")
    print(f"Health: {player.health}")
    print(f"Experience: {player.experience}")
    print(f"Gold: {player.gold}")
    print(f"Level: {player.level}")
    print(f"\nYour Backstory: {player.backstory}\n")

# Function to handle the encounter with a monster with dialogue choices and backstories
def encounter_monster_with_story(player):
    monster = random.choice(monsters)
    print(f"\nA wild {monster.name} appears! It is level {monster.level}.\n")
    
    dialogue_choice = input("What would you like to do? (1: Fight, 2: Run, 3: Talk): ")
    
    backstory = {
        "Goblin": "The goblin was stealing food for its hungry family.",
        "Zombie": "The zombie was once a brave knight, cursed into this form.",
        "Zombie Dog": "This poor dog was transformed by a dark spell.",
        "Orc": "The orc is a warrior exiled from its tribe, searching for redemption.",
        "Dragon": "The dragon is an ancient guardian of the forest's magic."
    }
    
    if dialogue_choice == '1':
        print("\nYou chose to fight!")
        if player.level >= monster.level:
            print("You defeated the monster!")
            player.experience += 10
            player.gold += 5
            print(f"You gained 10 experience and 5 gold. Your current experience is {player.experience} and gold is {player.gold}.")
            print(f"\nBackstory: {backstory[monster.name]}")
            print("You ponder on the reason behind the fight as you continue your quest.\n")
        else:
            print("The monster is too strong! You lose and take 10 damage.")
            player.health -= 10
            print(f"Your current health is {player.health}.\n")
    elif dialogue_choice == '2':
        print("\nYou chose to run away. Better safe than sorry!\n")
    elif dialogue_choice == '3':
        print("\nYou attempt to talk to the monster.")
        talk_outcome = random.choice([True, False])
        if talk_outcome:
            print("It seems you've calmed the monster down. It leaves you in peace.")
            print(f"\nBackstory: {backstory[monster.name]}")
            print("You realize that not all battles need to be fought.\n")
        else:
            print("The monster doesn't seem interested in talking. You have no choice but to run away, losing 5 health in the process.")
            player.health -= 5
            print(f"Your current health is {player.health}.\n")

# Sample main game loop with the new battle system, backstories, and character-specific stories
def main_game_with_full_story(num_encounters=5):
    show_expanded_introduction()
    introduce_quest()
    weapon_choice = choose_weapon()
    player = create_player_with_backstory(weapon_choice)
    show_initial_stats_and_backstory(player)
    
    for i in range(num_encounters):
        print(f"--- Encounter {i + 1} ---")
        encounter_monster_with_story(player)
        level_up(player)
    
    print("--- Final Boss Encounter ---")
    # Encounter the boss (omitted for brevity)

# Uncomment this line to run the game when you paste it into your local Python enviroment
main_game_with_full_story