from enemy import Enemy
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory
from item_factory import ItemFactory
from random import choice


class MonsterFactory:

    @staticmethod
    def create_monster(monster_type, level, rarity, difficulty):
        monster_configurations = {
            'wolf': {
                'health': 10,
                'exp': 5,
                'speed': 6,
                'gold': 5,
                'weapon': ('claw', 'basic'),
                'skills': (['bite'], 'basic'),
                'items': (['potion'], 'basic')
            },
            'bear': {
                'health': 17,
                'exp': 10,
                'speed': 5,
                'gold': 10,
                'weapon': ('swipe', 'basic'),
                'skills': (['bite'], 'basic'),
                'items': (['mana_potion'], 'basic')
            },
            'goblin': {
                'health': 8,
                'exp': 4,
                'speed': 8,
                'gold': 4,
                'weapon': ('dagger', 'basic'),
                'skills': (['slash', 'stab'], 'basic'),
                'items': (['potion'], 'basic')
            },
            'orc': {
                'health': 15,
                'exp': 8,
                'speed': 4,
                'gold': 8,
                'weapon': ('club', 'basic'),
                'skills': (['bash'], 'basic'),
                'items': (['mana_potion'], 'basic')
            },
            'troll': {
                'health': 20,
                'exp': 15,
                'speed': 3,
                'gold': 15,
                'weapon': ('club', 'basic'),
                'skills': (['bash', 'whack'], 'basic'),
                'items': (['elixir'], 'basic')
            }
            # Add more monsters as needed
        }

        if monster_type in monster_configurations:
            config = monster_configurations[monster_type]
            weapon = WeaponFactory.create_weapon(*config['weapon'])
            skills = SkillFactory.create_skills(*config['skills'])
            items = [ItemFactory.create_item(item, rarity) for item in config['items'][0]]

            return Enemy(monster_type.capitalize(), config['health'], config['exp'], level, config['speed'], config['gold'], weapon, skills, difficulty, items)
        else:
            raise ValueError(f'Unknown monster type: {monster_type}')

    @staticmethod
    def create_random_monsters(count, level, rarity, difficulty):
        monster_types = ['wolf', 'bear', 'goblin', 'orc', 'troll']
        return [MonsterFactory.create_monster(choice(monster_types), level, rarity, difficulty) for _ in range(count)]
