from weapon import Weapon


class WeaponFactory:

    @staticmethod
    def create_weapon(weapon_type, rarity):
        weapons = {
            'basic': {
                'sword': Weapon('Sword', 10, 4, 6, 10),
                'dagger': Weapon('Dagger', 6, 2, 10, 10),
                'staff': Weapon('Staff', 3, 5, 25, 10),
                'club': Weapon('Club', 5, 2, 2, 5),
                'claw': Weapon('Claw', 5, 1, 1, 0),
                'swipe': Weapon('Swipe', 8, 2, 3, 0)
            },
            'rare': {
                'sword': Weapon('Enchanted Sword', 15, 6, 8, 15),
                'dagger': Weapon('Poison Dagger', 10, 4, 12, 15),
                'staff': Weapon('Wizard Staff', 5, 7, 30, 15),
                'club': Weapon('War Club', 7, 3, 4, 8)
            }
            # Add more rarities as needed
        }

        if rarity in weapons and weapon_type in weapons[rarity]:
            return weapons[rarity][weapon_type]
        else:
            raise ValueError(f'Unknown weapon type or rarity: {weapon_type}, {rarity}')
