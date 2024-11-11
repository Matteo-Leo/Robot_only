import random
from typing import List, Dict

# Define base classes and setup for character creation
class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.exp = 0
        self.max_exp = 100
        self.inventory = []
        self.abilities = []
        self.hp = 100
        self.strength = 10
        self.defense = 10
        self.magic = 10
        self.update_stats()

    def update_stats(self):
        # Update stats based on class
        if self.char_class == "Wizard":
            self.magic += 15
        elif self.char_class == "Fighter":
            self.strength += 15
        elif self.char_class == "Barbarian":
            self.strength += 20
            self.hp += 10
        elif self.char_class == "Rogue":
            self.defense += 5
            self.strength += 10
        elif self.char_class == "Paladin":
            self.hp += 20
            self.defense += 15
        elif self.char_class == "Saint":
            self.hp += 30
            self.magic += 5
        elif self.char_class == "Warlock":
            self.magic += 20
        elif self.char_class == "Necromancer":
            self.magic += 20
            self.defense += 5

    def level_up(self):
        if self.exp >= self.max_exp:
            self.level += 1
            self.exp -= self.max_exp
            self.max_exp *= 1.1  # Increase required exp by 10%
            self.hp += 10
            self.strength += 5
            self.defense += 5
            self.magic += 5
            print(f"{self.name} leveled up to level {self.level}!")
            return True
        return False

    def gain_exp(self, amount):
        self.exp += amount
        leveled_up = self.level_up()
        if leveled_up:
            print(f"You are now level {self.level}!")

    def choose_ability(self, available_abilities):
        # Abilities unlocked by level; only available abilities can be chosen
        print("Choose a new ability:")
        for i, ability in enumerate(available_abilities):
            print(f"{i+1}. {ability['name']} - {ability['description']}")
        choice = int(input("Enter the number of the ability you want to choose: ")) - 1
        chosen_ability = available_abilities[choice]
        self.abilities.append(chosen_ability)
        print(f"{self.name} has learned {chosen_ability['name']}!")

# Define a simple Item system
class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, character):
        print(f"Using {self.name}...")
        self.effect(character)

# Define a basic storyline
def story_path(character):
    print("Welcome to the world of Eldoria, a land shrouded in mystery and danger...")
    choices = [
        {"prompt": "Help a lost villager", "outcome": "ally", "exp_gain": 20},
        {"prompt": "Attack a bandit camp", "outcome": "fight", "exp_gain": 30},
        {"prompt": "Explore the ancient ruins", "outcome": "mystery", "exp_gain": 25}
    ]
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice['prompt']}")
    choice = int(input("Choose an action: ")) - 1
    outcome = choices[choice]["outcome"]
    character.gain_exp(choices[choice]["exp_gain"])
    return outcome

# Implement a class-based ability dictionary
abilities = {
    "Wizard": [{"name": "Fireball", "description": "A blazing fire attack.", "level_required": 1}],
    "Fighter": [{"name": "Power Strike", "description": "A heavy attack.", "level_required": 1}],
    "Barbarian": [{"name": "Berserk", "description": "Increase strength temporarily.", "level_required": 1}],
    "Rogue": [{"name": "Backstab", "description": "High-damage attack if undetected.", "level_required": 1}],
    # Add more abilities for each class as needed
}

# Example of how a game might flow
def game():
    print("Welcome to the RPG game!")
    name = input("Enter your character's name: ")
    print("Choose your class: Wizard, Fighter, Barbarian, Rogue, Paladin, Saint, Warlock, Necromancer")
    char_class = input("Enter your class: ")
    player = Character(name, char_class)

    # Main game loop
    while player.level < 100:
        print("\n--- New Story Segment ---")
        outcome = story_path(player)

        # Trigger different actions based on the outcome
        if outcome == "ally":
            print("You have gained a new ally!")
        elif outcome == "fight":
            print("You engage in a fierce battle!")
        elif outcome == "mystery":
            print("You uncover a hidden secret in the ruins!")

        # Choose an ability if leveled up
        if player.level_up():
            available_abilities = [ab for ab in abilities[char_class] if ab['level_required'] <= player.level]
            if available_abilities:
                player.choose_ability(available_abilities)

        # Check for win/loss conditions (e.g., final boss based on story outcome)
        if player.level >= 10:  # Sample condition for final boss encounter
            print(f"{player.name} has reached the final confrontation with the antagonist!")
            break
    print("Game Over.")



# Define character classes with combat, leveling, and inventory systems
class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.exp = 0
        self.max_exp = 100
        self.inventory = []
        self.abilities = []
        self.hp = 100
        self.max_hp = 100
        self.strength = 10
        self.defense = 10
        self.magic = 10
        self.update_stats()

    def update_stats(self):
        # Update stats based on class
        class_stats = {
            "Wizard": {"magic": 15},
            "Fighter": {"strength": 15},
            "Barbarian": {"strength": 20, "hp": 10},
            "Rogue": {"strength": 10, "defense": 5},
            "Paladin": {"hp": 20, "defense": 15},
            "Saint": {"hp": 30, "magic": 5},
            "Warlock": {"magic": 20},
            "Necromancer": {"magic": 20, "defense": 5},
        }
        stats = class_stats.get(self.char_class, {})
        self.hp += stats.get("hp", 0)
        self.strength += stats.get("strength", 0)
        self.defense += stats.get("defense", 0)
        self.magic += stats.get("magic", 0)

    def level_up(self):
        if self.exp >= self.max_exp:
            self.level += 1
            self.exp -= self.max_exp
            self.max_exp = int(self.max_exp * 1.2)  # 20% more exp needed each level
            self.hp += 10
            self.max_hp += 10
            self.strength += 5
            self.defense += 5
            self.magic += 5
            print(f"{self.name} leveled up to level {self.level}!")
            return True
        return False

    def gain_exp(self, amount):
        self.exp += amount
        leveled_up = self.level_up()
        if leveled_up:
            self.choose_ability(abilities[self.char_class])
            print(f"You are now level {self.level}!")

    def choose_ability(self, available_abilities):
        available_choices = [ab for ab in available_abilities if ab['level_required'] <= self.level]
        if available_choices:
            print("Choose a new ability:")
            for i, ability in enumerate(available_choices):
                print(f"{i + 1}. {ability['name']} - {ability['description']}")
            choice = int(input("Enter the number of the ability you want to choose: ")) - 1
            chosen_ability = available_choices[choice]
            self.abilities.append(chosen_ability)
            print(f"{self.name} has learned {chosen_ability['name']}!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to inventory!")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                item.use(self)
                self.inventory.remove(item)
                return
        print("Item not found in inventory.")


# Define the Enemy class for combat
class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level * 30
        self.strength = level * 5
        self.defense = level * 3

    def attack(self):
        return max(0, self.strength - random.randint(0, 5))


# Define a basic combat function
def combat(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name} HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
        action = input("Choose action (attack, use item): ").lower()

        if action == "attack":
            # Player attacks
            player_attack = max(0, player.strength - enemy.defense + random.randint(-5, 5))
            enemy.hp -= player_attack
            print(f"{player.name} deals {player_attack} damage to {enemy.name}!")

        elif action == "use item":
            item_name = input("Enter item name to use: ")
            player.use_item(item_name)

        # Enemy's turn to attack if still alive
        if enemy.hp > 0:
            enemy_attack = enemy.attack()
            player.hp -= max(0, enemy_attack - player.defense)
            print(f"{enemy.name} deals {enemy_attack} damage to {player.name}!")

    # Outcome of the battle
    if player.hp > 0:
        print(f"{player.name} defeated {enemy.name}!")
        player.gain_exp(enemy.level * 50)
    else:
        print("You were defeated...")
        player.hp = player.max_hp  # Revive player at full HP (for simplicity)


# Define an Item class with specific effects
class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, character):
        print(f"Using {self.name}...")
        self.effect(character)


# Define healing potion effect
def heal(character):
    healing_amount = 50
    character.hp = min(character.max_hp, character.hp + healing_amount)
    print(f"{character.name} healed for {healing_amount} HP!")


# Sample abilities
abilities = {
    "Wizard": [{"name": "Fireball", "description": "A blazing fire attack.", "level_required": 1}],
    "Fighter": [{"name": "Power Strike", "description": "A heavy attack.", "level_required": 1}],
    "Barbarian": [{"name": "Berserk", "description": "Increase strength temporarily.", "level_required": 1}],
    "Rogue": [{"name": "Backstab", "description": "High-damage attack if undetected.", "level_required": 1}],
    # Add more abilities for each class as needed
}


# Example game function with combat and inventory use
def game():
    print("Welcome to the RPG game!")
    name = input("Enter your character's name: ")
    print("Choose your class: Wizard, Fighter, Barbarian, Rogue, Paladin, Saint, Warlock, Necromancer")
    char_class = input("Enter your class: ")
    player = Character(name, char_class)

    # Add initial items
    potion = Item("Healing Potion", "Restores 50 HP.", heal)
    player.add_item(potion)

    # Main game loop with combat encounter
    while player.level < 100:
        print("\n--- New Story Segment ---")
        outcome = story_path(player)

        # Encounter an enemy based on outcome
        if outcome == "fight":
            enemy = Enemy("Bandit", player.level)
            combat(player, enemy)

        # Check for win/loss conditions
        if player.level >= 10:  # Final encounter as an example
            print(f"{player.name} has reached the final confrontation with the antagonist!")
            break
    print("Game Over.")


# Run the game
game()
