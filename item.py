class Item:
    def __init__(self, name, use_function, value):
        self.name = name
        self.use_function = use_function
        self.value = value

    def use(self, target):
        return self.use_function(target)


def potion_use(player):
    player.health += 10  # Heals 10 health points
    player.health = min(player.max_health, player.health)  # Ensure health does not exceed max health
    print(f'{player.name} used a potion and gained 10 health points.')


def elixir_use(player):
    player.health += 5  # Heals 5 health points
    player.weapon.energy += 5 # Restores 10 energy points
    player.health = min(player.max_health, player.health)  # Ensure health does not exceed max health
    print(f'{player.name} used an elixir and gained 50 health points.')


def mana_potion_use(player):
    player.weapon.energy += 10  # Restores 10 energy points
    player.weapon.energy = min(player.weapon.max_energy, player.weapon.energy)  # Ensure energy does not exceed max
    print(f'{player.name} used a mana potion and gained 30 energy points.')
