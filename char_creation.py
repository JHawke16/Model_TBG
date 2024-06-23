from weapon_factory import WeaponFactory
from skill_factory import SkillFactory
from player import Player


class CharCreation:

    def char_create(self):
        class_configurations = {
            '1': {
                'class_name': 'Warrior',
                'health': 50,
                'speed': 10,
                'weapon': 'sword',
                'skills': ['slash', 'swing', 'stab']
            },
            '2': {
                'class_name': 'Rogue',
                'health': 30,
                'speed': 20,
                'weapon': 'dagger',
                'skills': ['backstab', 'silent_strike', 'sap']
            },
            '3': {
                'class_name': 'Mage',
                'health': 25,
                'speed': 7,
                'weapon': 'staff',
                'skills': ['fireball', 'flames', 'magma', 'blaze']
            },
            '4': {
                'class_name': 'Commoner',
                'health': 15,
                'speed': 5,
                'weapon': 'club',
                'skills': ['bash', 'whack']
            }
        }

        print('\nWelcome to Character Creation')

        while True:
            choice = input('\n1. Warrior\n2. Rogue\n3. Mage\n4. Commoner\nChoice: ')
            config = class_configurations.get(choice)
            if config:
                p_weapon = WeaponFactory.create_weapon(config['weapon'], 'basic')
                print(f"\n{config['class_name']} stats:")
                print(f"Weapon - {p_weapon.name} (Energy: {p_weapon.energy}/{p_weapon.max_energy})")
                print(f"Skills - {', '.join(config['skills']).title()}")
                print(f"Health = {config['health']}")
                print(f"Speed = {config['speed']}")

                choice_confirm = input(f'\nWould you like to select the {config["class_name"]}? (y/n)\nChoice: ')
                if choice_confirm.lower() == 'y':
                    print(f'\n{config["class_name"]} Selected!')
                    p_name = input('Please enter a name for your character\nName: ')
                    p_skills = SkillFactory.create_skills(config['skills'], 'basic')
                    player = Player(p_name, config['health'], 0, 1, 0, config['speed'], p_weapon, p_skills)
                    print('\nStarting Tutorial Battle\n')
                    return player
                elif choice_confirm.lower() == 'n':
                    print('Returning to character selection')
            else:
                print('Invalid choice, please select a valid class.')
