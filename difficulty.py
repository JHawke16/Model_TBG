class Difficulty:

    def __init__(self, value):
        self.value = value

    def damage_scaler(self, damage):
        scaled_damage = damage + ((self.value - 1) * damage * 0.3)
        return scaled_damage

    def exp_scaler(self, exp):
        scaled_exp = exp + ((self.value - 1) * exp * 0.3)
        return scaled_exp

    def gold_scaler(self, gold):
        scaled_gold = gold + ((self.value - 1) * gold * 0.2)
        return scaled_gold

    def health_scaler(self, health):
        scaled_health = health + ((self.value - 1) * health * 0.3)
        return scaled_health
