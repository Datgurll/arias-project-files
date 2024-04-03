from characters import Player, initial_attributes, character_backstories
from monsters import basic_monsters, elite_monsters, boss_monsters
from encounters import encounter_monster_with_story

# Function to create a new player with a backstory
def create_player_with_backstory(weapon_choice):
    weapon_to_class = {
        "staff": "Mage",
        "sword": "Knight",
        "gun": "Thief",
        "nunchuks": "Monk",
        "shoes": "Speeder",
        "horn": "Windmaster",  # New character class
        "bow": "Archer",  # Another new character class
    }
    player_class = weapon_to_class.get(weapon_choice.lower(), "Commoner")  # Case-insensitive, defaults to "Commoner"
    attrs = initial_attributes.get(player_class, {})  # Get attributes safely
    return Player(player_class, weapon_choice, attrs.get("health", 100), attrs.get("experience", 0), attrs.get("gold", 0), attrs.get("level", 1), character_backstories.get(player_class, "A mysterious stranger with no past."))

# List of completed quests and decisions
completed_quests = []
decisions_made = []

# Random events that can occur between encounters
random_events = [
    "You stumble upon an ancient shrine. Do you pray? (yes/no)",
    "A beggar asks for some gold. Do you give him some? (yes/no)",
    "You find a mysterious potion on the ground. Do you drink it? (yes/no)",
    "You encounter a wandering merchant. Do you trade? (yes/no)"  # New random event
]

# Chapter One: The Journey Begins
def start_chapter_one(player):
    print("\nChapter One: The Journey Begins")
    print(f"{player.backstory}")
    decision_1 = input("Do you want to explore the forest or stay near the village? (explore/stay): ").lower()
    decision_2 = input("You see a fork in the road. Do you go left or right? (left/right): ").lower()
    
    if decision_1 == 'explore':
        print("You venture deep into the forest, unaware of the dangers that lie ahead.")
        decisions_made.append("Explored the Forest")
    elif decision_1 == 'stay':
        print("You decide to stay near the village and help the locals.")
        decisions_made.append("Helped the Village")
    
    if decision_2 == 'left':
        print("You take the path to the left and find a hidden treasure!")
        decisions_made.append("Went Left")
    elif decision_2 == 'right':
        print("You take the path to the right and are ambushed by goblins!")
        decisions_made.append("Went Right")
    
    # New Chapter Two: The Quest Continues
    print("\nChapter Two: The Quest Continues")
    decision_3 = input("You come across a river. Do you swim across or find a bridge? (swim/bridge): ").lower()
    if decision_3 == 'swim':
        print("You bravely swim across the river but lose some energy.")
        decisions_made.append("Swam the River")
    elif decision_3 == 'bridge':
        print("You find a bridge and safely cross the river.")
        decisions_made.append("Crossed the Bridge")
    
    # Implement the encounter function after each decision to add more dynamic interactions
    encounter_monster_with_story(player, basic_monsters, elite_monsters, boss_monsters, random_events)

# Call this function to start the game
if __name__ == "__main__":
    print("Welcome to the Adventure Game!")
    weapon_choice = input("Choose your weapon (staff, sword, gun, nunchuks, shoes, horn, bow): ")
    player = create_player_with_backstory(weapon_choice)
    start_chapter_one(player)
