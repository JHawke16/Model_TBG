from difficulty import Difficulty

difficulty = Difficulty(1)


class Enemy:

    def __init__(self, health, exp, level, weapon=None):
        self.health = health
        self.exp = exp
        self.level = level
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            damage = round(difficulty.damage_scaler(self.weapon.damage))
            print(f'\nEnemy Attacks for {damage} damage')
            return damage
        else:
            return 0

    def take_damage(self, damage):
        self.health -= damage
        print(f'\nEnemy Remaining Health: {self.health}\n')
        self.check_alive()

    def check_alive(self):
        return self.health > 0

    def drop_exp(self):
        self.check_alive()
        dropped_exp = round(difficulty.exp_scaler(self.exp))
        print(f'Enemy dropped {dropped_exp} exp')
        return dropped_exp
