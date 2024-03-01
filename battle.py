from player import Player
from enemy import Enemy
from weapon_factory import WeaponFactory

p_weapon = WeaponFactory.create_weapon('sword')
e_weapon = WeaponFactory.create_weapon('claw')
player = Player(15, 0, 1, p_weapon)
enemy = Enemy(20, 60, 1, e_weapon)


class Battle:

    def battle(self, player, enemy):
        while player.check_alive() and enemy.check_alive():
            print('\nPlayer Health:', player.health)
            print('Enemy Health:', enemy.health)

            choice = input('\nDo you want to attack?\nChoice: ')
            if choice == 'y':
                player.take_damage(enemy.attack())
                if not player.check_alive():
                    print('Battle Over')

                enemy.take_damage(player.attack())
                if not enemy.check_alive():
                    exp = enemy.drop_exp()
                    player.gain_exp(exp)

    def start_battle(self):
        self.battle(player, enemy)
