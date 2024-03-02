from char_creation import CharCreation
from monster_factory import MonsterFactory
from battle_factory import BattleFactory


class GameLoop:

    def start_game(self, player):
        # Start tutorial battle
        self.start_tutorial_battle(player)

    def start_tutorial_battle(self, player):
        enemy = MonsterFactory.create_basic_monster('wolf')  # Initialize the tutorial enemy
        battle = BattleFactory.create_battle(player, enemy)  # Create the battle
        battle.start_battle()  # Start the battle
