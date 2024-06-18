import random


class Player:

    def __init__(self, name, health, base_exp, level, gold, speed, weapon=None, skills=None):
        self.name = name
        self.base_health = health
        self.health = health
        self.base_exp = base_exp
        self.level = level
        self.required_exp = self.level * 10
        self.max_health = self.base_health + ((self.level - 1) * 5)
        self.gold = gold
        self.speed = speed
        self.weapon = weapon
        self.skills = skills if skills else []
        self.is_defending = False  # Attribute to track defending state

    def attack(self):
        if self.weapon:
            print(f'\n{self.name} Attacks for {self.weapon.damage} damage')
            return self.weapon.damage
        else:
            return 0

    def skill_attack(self):
        while True:  # Keep asking until a valid skill is chosen or the user decides to go back.
            if self.skills and self.weapon:
                print(f'\nEnergy Remaining: {self.weapon.energy}')
                print("\nAvailable skills:")
                for index, skill in enumerate(self.skills, start=1):
                    print(f"{index}. {skill.name} (Damage: {skill.damage}, Energy Cost: {skill.energy})")

                choice = input('Choose a skill by number (or type "back" to choose another action): ')
                if choice.lower() == "back":  # Allow the user to go back and choose another action.
                    return None

                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(self.skills):
                        selected_skill = self.skills[choice_index]
                        if self.weapon.energy >= selected_skill.energy:
                            self.weapon.energy -= selected_skill.energy
                            print(
                                f'\n{self.name} uses {selected_skill.name} for {selected_skill.damage} damage, '
                                f'costing {selected_skill.energy} energy')
                            print(f'Remaining Weapon Energy: {self.weapon.energy}')
                            return selected_skill.damage
                        else:
                            print(
                                'Not enough energy to use this skill. '
                                'Choose again or type "back" to choose another action.')
                    else:
                        print('Invalid choice. Please select a valid skill number.')
                except ValueError:
                    print('Please enter a valid number or type "back" to choose another action.')
            else:
                print('No skills available or no weapon equipped.')
                return None

    def take_damage(self, damage):
        if self.is_defending and self.weapon:
            damage -= self.weapon.defense  # Apply defense reduction
            damage = max(damage, 0)  # Ensure damage doesn't go below 0
        self.health -= damage
        print(f'\n{self.name} Remaining Health: {self.health}')
        self.check_alive()

    def check_alive(self):
        return self.health > 0

    def gain_gold(self, gold):
        self.gold += gold
        print(f'Total gold: {self.gold}\n')

    def gain_exp(self, exp):
        self.base_exp += exp
        self.level_up()

    def level_up(self):
        check_level = self.required_exp - self.base_exp
        while self.base_exp >= self.required_exp:
            self.level += 1
            self.speed += 2
            carry_over = self.base_exp - self.required_exp
            self.base_exp = carry_over
            self.required_exp = self.level * 10
            self.max_health = self.base_health + ((self.level - 1) * 5)
            self.health = self.max_health  # Set current health to max health
            print(f'{self.name} Levels up!')
            print(f'{self.name} Max Health: {self.max_health} HP')
        print(f'\n{self.name} Level: {self.level}')
        print(f'Current exp: {self.base_exp}')
        print(f'Exp required for level up: {check_level}\n')

    def reset_stats(self):
        self.health = self.max_health
        self.is_defending = False  # Reset defending state
        if self.weapon:
            self.weapon.energy = self.weapon.max_energy

    def defend(self):
        self.is_defending = True
        print(f'{self.name} is defending, reducing incoming damage by {self.weapon.defense}')

    def flee(self):
        if random.random() < 0.2:  # 20% chance to flee successfully
            print(f'{self.name} successfully flees the battle!')
            return True
        else:
            print(f'{self.name} failed to flee.')
            return False

