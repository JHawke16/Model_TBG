import random
from random import choice
from difficulty import Difficulty


class Enemy:
    def __init__(self, name, health, exp, level, speed, gold, weapon=None, skills=None, difficulty=None, drop_items=None):
        self.name = name
        self.health = round(difficulty.health_scaler(health)) if difficulty else health
        self.max_health = self.health  # Setting max_health equal to initial health
        self.exp = exp
        self.level = level
        self.speed = speed
        self.gold = gold
        self.weapon = weapon
        self.skills = skills if skills else []
        self.difficulty = difficulty if difficulty else Difficulty(1)  # Default to difficulty level 1
        self.is_defending = False  # Attribute to track defending state
        self.drop_items = drop_items if drop_items else []

    def attack(self):
        if self.weapon:
            damage = round(self.difficulty.damage_scaler(self.weapon.damage))
            print(f'\n{self.name} Attacks for {damage} damage')
            return damage
        else:
            return 0

    def skill_attack(self):
        if self.skills and self.weapon:
            selected_skill = choice(self.skills)  # Randomly choose a skill
            if self.weapon.energy >= selected_skill.energy:
                self.weapon.energy -= selected_skill.energy
                damage = round(self.difficulty.skill_damage_scaler(selected_skill.damage))
                print(f'\n{self.name} uses {selected_skill.name} for {damage} damage, costing {selected_skill.energy} energy')
                return damage
            else:
                print(f'\n{self.name} does not have enough energy to use any skill, performing a normal attack instead.')
                return self.attack()
        return self.attack()  # If no skills are available, perform a normal attack

    def take_damage(self, damage):
        if self.is_defending and self.weapon:
            damage -= self.weapon.defense  # Apply defense reduction
            damage = max(damage, 0)  # Ensure damage doesn't go below 0
        self.health -= damage
        print(f'\n{self.name} took {damage} damage, Remaining Health: {self.health}')
        self.check_alive()

    def check_alive(self):
        return self.health > 0

    def drop_gold(self):
        self.check_alive()
        dropped_gold = round(self.difficulty.gold_scaler(self.gold))
        print(f'{self.name} dropped {dropped_gold} gold')
        return dropped_gold

    def drop_exp(self):
        self.check_alive()
        dropped_exp = round(self.difficulty.exp_scaler(self.exp))
        print(f'{self.name} dropped {dropped_exp} exp')
        return dropped_exp

    def drop_item(self):
        if self.drop_items and random.random() < 0.4:  # 40% chance to drop an item
            return choice(self.drop_items)
        return None

    def flee(self):
        if self.health / self.max_health < 0.15 and random.random() < 0.2:  # 15% health and 20% flee chance
            print(f'{self.name} successfully flees the battle!')
            return True
        else:
            print(f'{self.name} failed to flee.')
            return False

    def reset_defense(self):
        self.is_defending = False

    def defend(self):
        self.is_defending = True
        print(f'{self.name} is defending, reducing incoming damage by {self.weapon.defense}')
