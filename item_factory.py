from item import Item, potion_use, elixir_use, mana_potion_use


class ItemFactory:
    @staticmethod
    def create_item(item_type):
        items = {
            'potion': Item('Health Potion', potion_use, 20),
            'elixir': Item('Elixir', elixir_use, 50),
            'mana_potion': Item('Mana Potion', mana_potion_use, 30),
        }

        if item_type in items:
            return items[item_type]
        else:
            raise ValueError(f'Unknown item type: {item_type}')
