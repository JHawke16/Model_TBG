from weapon import Weapon


class WeaponFactory:

    @staticmethod
    def create_weapon(weapon_type):
        weapons = {
            'sword': Weapon('Sword', 10, 4, 3, 10),
            'dagger': Weapon('Dagger', 6, 2, 5, 10),
            'staff': Weapon('Staff', 3, 5, 15, 10),
            'club': Weapon('Club', 5, 2, 2, 5),
            'claw': Weapon('Claw', 5, 1, 1, 0)

        }

        if weapon_type in weapons:
            return weapons[weapon_type]
        else:
            raise ValueError(f'Unknown weapon type: {weapon_type}')
