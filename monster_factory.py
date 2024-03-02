from enemy import Enemy
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory


class MonsterFactory:

    @staticmethod
    def create_basic_monster(monster_type, difficulty):
        # Skills needs to be added as a list even if single one
        # Wolf gear
        w_wolf = WeaponFactory.create_weapon('claw')
        s_wolf = SkillFactory.create_skills(['bite'])
        # Bear gear
        w_bear = WeaponFactory.create_weapon('swipe')
        s_bear = SkillFactory.create_skills(['bite'])
        basic_monster = {
            'wolf': Enemy('Wolf', 10, 5, 1, 6, 5, w_wolf, s_wolf, difficulty),
            'bear': Enemy('Bear', 17, 10, 2, 5, 10, w_bear, s_bear, difficulty)
        }

        if monster_type in basic_monster:
            return basic_monster[monster_type]
        else:
            raise ValueError(f'Unknown weapon type: {monster_type}\nCheck if forgot to add the skill as a list')
