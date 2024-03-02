from difficulty import Difficulty

difficulty = Difficulty(1)


class Enemy:

    def __init__(self, name, health, exp, level, speed, weapon=None, skills=None):
        self.name = name
        self.health = health
        self.exp = exp
        self.level = level
        self.speed = speed
        self.weapon = weapon
        self.skills = skills if skills else []

    def attack(self):
        if self.weapon:
            damage = round(difficulty.damage_scaler(self.weapon.damage))
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

    def drop_exp(self):
        self.check_alive()
        dropped_exp = round(difficulty.exp_scaler(self.exp))
        print(f'{self.name} dropped {dropped_exp} exp')
        return dropped_exp
