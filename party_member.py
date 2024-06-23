from random import choice


class PartyMember:
    def __init__(self, name, health, level, speed, weapon=None, skills=None):
        self.name = name
        self.base_health = health
        self.health = health
        self.level = level
        self.required_exp = self.level * 10
        self.base_exp = 0
        self.max_health = self.base_health + ((self.level - 1) * 5)
        self.speed = speed
        self.weapon = weapon
        self.skills = skills if skills else []
        self.is_defending = False

    def attack(self):
        if self.weapon:
            print(f'\n{self.name} Attacks for {self.weapon.damage} damage')
            return self.weapon.damage
        else:
            return 0

    def skill_attack(self):
        if self.skills and self.weapon:
            selected_skill = choice(self.skills)
            if self.weapon.energy >= selected_skill.energy:
                self.weapon.energy -= selected_skill.energy
                print(
                    f'\n{self.name} uses {selected_skill.name} for {selected_skill.damage}'
                    f' damage, costing {selected_skill.energy} energy')
                print(f'Remaining Weapon Energy: {self.weapon.energy}')
                return selected_skill.damage
            else:
                print(f'{self.name} does not have enough energy to use any skill, performing a normal attack instead.')
                return self.attack()
        return self.attack()

    def take_damage(self, damage):
        if self.is_defending and self.weapon:
            damage -= self.weapon.defense
            damage = max(damage, 0)
        self.health -= damage
        print(f'\n{self.name} took {damage} damage, Remaining Health: {self.health}')
        self.check_alive()

    def check_alive(self):
        return self.health > 0

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
