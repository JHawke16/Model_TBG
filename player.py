class Player:

    def __init__(self, name, health, base_exp, level, gold, speed, weapon=None, skills=None):
        self.name = name
        self.health = health
        self.base_exp = base_exp
        self.level = level
        self.required_exp = self.level * 10
        self.max_health = self.health + ((self.level - 1) * 5)
        self.gold = gold
        self.speed = speed
        self.weapon = weapon
        self.skills = skills if skills else []

    def attack(self):
        if self.weapon:
            print(f'\n{self.name} Attacks for {self.weapon.damage} damage')
            return self.weapon.damage
        else:
            return 0

    def take_damage(self, damage):
        self.health -= damage
        print(f'\n{self.name} Remaining Health: {self.health}')
        self.check_alive()

    def check_alive(self):
        return self.health > 0

    def gain_exp(self, exp):
        self.base_exp += exp
        print(f'Total exp: {self.base_exp}')
        self.reset_health()
        self.level_up()

    def level_up(self):
        while self.base_exp >= self.required_exp:
            self.level += 1
            carry_over = self.base_exp - self.required_exp
            self.base_exp = carry_over
            self.required_exp = self.level * 10
            self.max_health = self.health + ((self.level - 1) * 5)
            self.reset_health()
            check_level = self.required_exp - self.base_exp
        print(f'{self.name} Level: {self.level}')
        print(f'Current exp: {self.base_exp}')
        print(f'Exp required for level up: {check_level}')
        print(f'\n{self.name} Max Health increased: {self.health}')

    def reset_health(self):
        self.health = self.max_health
