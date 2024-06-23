import random
from inventory import Inventory
# from party_member import PartyMember


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
        self.inventory = Inventory()
        self.party_members = []  # Initialize party members list
        self.is_defending = False

    def attack(self):
        if self.weapon:
            print(f'\n{self.name} Attacks for {self.weapon.damage} damage')
            return self.weapon.damage
        else:
            return 0

    def skill_attack(self):
        while True:
            if self.skills and self.weapon:
                print(f'\nEnergy Remaining: {self.weapon.energy}')
                print("\nAvailable skills:")
                for index, skill in enumerate(self.skills, start=1):
                    print(f"{index}. {skill.name} (Damage: {skill.damage}, Energy Cost: {skill.energy})")

                choice = input('Choose a skill by number (or type "back" to choose another action): ')
                if choice.lower() == "back":
                    return None

                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(self.skills):
                        selected_skill = self.skills[choice_index]
                        if self.weapon.energy >= selected_skill.energy:
                            self.weapon.energy -= selected_skill.energy
                            print(
                                f'\n{self.name} uses {selected_skill.name} for {selected_skill.damage}'
                                f' damage, costing {selected_skill.energy} energy')
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
            damage -= self.weapon.defense
            damage = max(damage, 0)
        self.health -= damage
        print(f'\n{self.name} took {damage} damage, Remaining Health: {self.health}')
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
        leveled_up = False
        while self.base_exp >= self.required_exp:
            self.level += 1
            self.speed += 2
            carry_over = self.base_exp - self.required_exp
            self.base_exp = carry_over
            self.required_exp = self.level * 10
            self.max_health = self.base_health + ((self.level - 1) * 5)
            self.health = self.max_health
            if self.weapon:
                self.weapon.energy = self.weapon.max_energy
            print(f'{self.name} Levels up!')
            print(f'{self.name} Max Health: {self.max_health} HP')
            leveled_up = True
        if leveled_up:
            check_level = self.required_exp - self.base_exp
            print(f'\n{self.name} Level: {self.level}')
            print(f'Current exp: {self.base_exp}')
            print(f'Exp required for level up: {check_level}\n')

    def reset_stats(self):
        self.health = self.max_health
        self.is_defending = False
        if self.weapon:
            self.weapon.energy = self.weapon.max_energy

    def reset_defense(self):
        self.is_defending = False

    def defend(self):
        self.is_defending = True
        print(f'{self.name} is defending, reducing incoming damage by {self.weapon.defense}')

    def flee(self):
        if random.random() < 0.2:
            print(f'{self.name} successfully flees the battle!')
            return True
        else:
            print(f'{self.name} failed to flee.')
            return False

    def exit_defend(self):
        self.is_defending = False

    def use_item(self, item_name):
        item = self.inventory.get_item(item_name)
        if item:
            item.use(self)
            self.inventory.remove_item(item)
            self.exit_defend()
            return True
        else:
            print(f'Cannot use {item_name}.')
            return False

    def heal(self, amount):
        self.health += amount
        self.health = min(self.max_health, self.health)
        print(f'{self.name} healed for {amount} health points. Current health: {self.health}')

    def restore_energy(self, amount):
        if self.weapon:
            self.weapon.energy += amount
            self.weapon.energy = min(self.weapon.max_energy, self.weapon.energy)
            print(
                f'{self.name} restored {amount} energy points. '
                f'Current energy: {self.weapon.energy}')

    def add_party_member(self, party_member):
        self.party_members.append(party_member)
        print(f'{party_member.name} has joined your party!')

    def view_party_members(self):
        if not self.party_members:
            print("No party members in your party.")
        else:
            print("Party members:")
            for member in self.party_members:
                exp_to_next_level = member.required_exp - member.base_exp
                print(f"- {member.name} (Level {member.level})")
                print(f"  Health: {member.health}/{member.max_health}")
                print(f"  Exp: {member.base_exp}/{member.required_exp}")
                print(f"  Exp to next level: {exp_to_next_level}")
                print(f"  Speed: {member.speed}")
                if member.weapon:
                    print(f"  Weapon: {member.weapon.name} (Damage: {member.weapon.damage}, Defense: {member.weapon.defense}, "
                          f"Energy: {member.weapon.energy}/{member.weapon.max_energy})")
                if member.skills:
                    print("  Skills:")
                    for skill in member.skills:
                        print(f"- {skill.name} (Damage: {skill.damage}, Energy Cost: {skill.energy})")

    def distribute_exp(self, exp):
        total_members = len(self.party_members) + 1  # Include player
        exp_per_member = exp // total_members
        self.gain_exp(exp_per_member)
        for member in self.party_members:
            member.gain_exp(exp_per_member)
