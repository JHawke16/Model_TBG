from weapon import Weapon


class WeaponFactory:

    @staticmethod
    def create_weapon(weapon_type, rarity):
        weapons = {
            'basic': {
                'sword': Weapon('Sword', 'sword', 10, 6, 6, 10),
                'dagger': Weapon('Dagger', 'dagger', 6, 10, 10, 3),
                'staff': Weapon('Staff', 'staff', 3, 25, 25, 5),
                'club': Weapon('Club', 'club', 5, 2, 2, 5),
                'claw': Weapon('Claw', 'claw', 5, 1, 1, 0),
                'swipe': Weapon('Swipe', 'claw', 8, 3, 3, 0)
            },
            'rare': {
                'sword': Weapon('Enchanted Sword', 'sword', 15, 6, 8, 15),
                'dagger': Weapon('Poison Dagger', 'dagger', 10, 4, 12, 15),
                'staff': Weapon('Wizard Staff', 'staff', 5, 7, 30, 15),
                'club': Weapon('War Club', 'club', 15, 3, 4, 8)
            }
            # Add more rarities as needed
        }

        if rarity in weapons and weapon_type in weapons[rarity]:
            return weapons[rarity][weapon_type]
        else:
            raise ValueError(f'Unknown weapon type or rarity: {weapon_type}, {rarity}')

