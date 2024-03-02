from difficulty import Difficulty


class Enemy:

    def __init__(self, name, health, exp, level, speed, gold, weapon=None, skills=None, difficulty=None):
        self.name = name
        self.health = health
        self.exp = exp
        self.level = level
        self.speed = speed
        self.gold = gold
        self.weapon = weapon
        self.skills = skills if skills else []
        self.difficulty = difficulty if difficulty else Difficulty(1)  # Default to difficulty level 1

    def attack(self):
        if self.weapon:
            damage = round(self.difficulty.damage_scaler(self.weapon.damage))
            print(f'\n{self.name} Attacks for {damage} damage')
            return damage
        else:
            return 0

    def take_damage(self, damage):
        self.health -= damage
        print(f'\n{self.name} Remaining Health: {self.health}\n')
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
