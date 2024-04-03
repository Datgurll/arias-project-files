
class Player:
    def __init__(self, player_class, weapon, health, experience, gold, level, backstory):
        self.player_class = player_class
        self.weapon = weapon
        self.health = health
        self.experience = experience
        self.gold = gold
        self.level = level
        self.backstory = backstory
        self.special_ability = None

    def level_up(self):
        if self.experience >= 20:
            print("Congratulations, you leveled up!")
            self.level += 1
            self.health += 10
            self.experience = 0
            if self.level == 2:
                self.unlock_special_ability()

    def unlock_special_ability(self):
        abilities = {
            "Mage": "Fireball",
            "Knight": "Shield Bash",
            "Thief": "Stealth",
            "Monk": "Meditate"
        }
        self.special_ability = abilities.get(self.player_class)
        print(f"You've unlocked a special ability: {self.special_ability}")

initial_attributes = {
    "Mage": {"health": 80, "experience": 0, "gold": 20, "level": 1},
    "Knight": {"health": 100, "experience": 0, "gold": 15, "level": 1},
    "Thief": {"health": 90, "experience": 0, "gold": 25, "level": 1},
    "Monk": {"health": 95, "experience": 0, "gold": 20, "level": 1}
}

character_backstories = {
    "Mage": "Born in 'The Land of the Silent', you were fascinated by magical books...",
    "Knight": "You are the last heir to a fallen noble house in the 'Kingdom of the Hills'...",
    "Thief": "Growing up on the streets of the '3rd Ward', you had to steal to survive...",
    "Monk": "Raised in a secluded monastery, whose name is known to none..."
}
