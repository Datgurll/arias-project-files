
class Monster:
    def __init__(self, name, level, health, special_ability=None):
        self.name = name
        self.level = level
        self.health = health
        self.special_ability = special_ability

# Different types of monsters
basic_monsters = [
    Monster("Goblin", 1, 20),
    Monster("Zombie", 2, 30),
    Monster("Zombie Dog", 3, 25),
]

elite_monsters = [
    Monster("Orc", 4, 50, special_ability="Berserk"),
    Monster("Dragon", 5, 100, special_ability="Fire Breath")
]

boss_monsters = [
    Monster("Lich King", 6, 200, special_ability="Necromancy"),
    Monster("Queen of Shadows", 7, 250, special_ability="Shadow Manipulation")
]
