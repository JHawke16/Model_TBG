from enemy import Enemy
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory


class MonsterFactory:

    @staticmethod
    def create_basic_monster(monster_type):
        w_wolf = WeaponFactory.create_weapon('claw')
        s_wolf = SkillFactory.create_skills(['bite'])
        basic_monster = {
            'wolf': Enemy('Wolf', 15, 10, 1, 6, w_wolf, s_wolf)
        }

        if monster_type in basic_monster:
            return basic_monster[monster_type]
        else:
            raise ValueError(f'Unknown weapon type: {monster_type}')
