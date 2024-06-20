from enemy import Enemy
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory
from item_factory import ItemFactory
from random import choice


class MonsterFactory:

    @staticmethod
    def create_basic_monster(monster_type, difficulty):
        # Skills needs to be added as a list even if single one
        w_wolf = WeaponFactory.create_weapon('claw')
        s_wolf = SkillFactory.create_skills(['bite'])
        i_wolf = [ItemFactory.create_item('potion')]

        w_bear = WeaponFactory.create_weapon('swipe')
        s_bear = SkillFactory.create_skills(['bite'])
        i_bear = [ItemFactory.create_item('potion')]

        w_goblin = WeaponFactory.create_weapon('dagger')
        s_goblin = SkillFactory.create_skills(['slash', 'stab'])
        i_goblin = [ItemFactory.create_item('potion')]

        w_orc = WeaponFactory.create_weapon('club')
        s_orc = SkillFactory.create_skills(['bash'])
        i_orc = [ItemFactory.create_item('potion')]

        w_troll = WeaponFactory.create_weapon('club')
        s_troll = SkillFactory.create_skills(['bash', 'whack'])
        i_troll = [ItemFactory.create_item('potion')]

        basic_monster = {
            'wolf': Enemy('Wolf', 10, 5, 1, 6, 5, w_wolf, s_wolf, difficulty, i_wolf),
            'bear': Enemy('Bear', 17, 10, 2, 5, 10, w_bear, s_bear, difficulty, i_bear),
            'goblin': Enemy('Goblin', 8, 4, 1, 8, 4, w_goblin, s_goblin, difficulty, i_goblin),
            'orc': Enemy('Orc', 15, 8, 2, 4, 8, w_orc, s_orc, difficulty, i_orc),
            'troll': Enemy('Troll', 20, 15, 3, 3, 15, w_troll, s_troll, difficulty, i_troll)
        }

        if monster_type in basic_monster:
            return basic_monster[monster_type]
        else:
            raise ValueError(f'Unknown monster type: {monster_type}')

    @staticmethod
    def create_random_monsters(count, difficulty):
        monster_types = ['wolf', 'bear', 'goblin', 'orc', 'troll']
        return [MonsterFactory.create_basic_monster(choice(monster_types), difficulty) for _ in range(count)]
