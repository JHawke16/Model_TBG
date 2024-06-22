from item import Item


class ItemFactory:

    @staticmethod
    def create_item(item_type, rarity):
        items = {
            'basic': {
                'potion': Item('Health Potion', lambda player: player.heal(20), 20),
                'mana_potion': Item('Mana Potion', lambda player: player.restore_energy(20), 30),
                'elixir': Item('Elixir', lambda player: (player.heal(30), player.restore_energy(30)), 50)
            },
            'rare': {
                'potion': Item('Greater Health Potion', lambda player: player.heal(50), 50),
                'mana_potion': Item('Greater Mana Potion', lambda player: player.restore_energy(50), 50),
                'elixir': Item('Greater Elixir', lambda player: (player.heal(60), player.restore_energy(60)), 80)
            }
            # Add more rarities as needed
        }

        if rarity in items and item_type in items[rarity]:
            return items[rarity][item_type]
        else:
            raise ValueError(f'Unknown item type or rarity: {item_type}, {rarity}')
