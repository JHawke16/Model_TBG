from monster_factory import MonsterFactory
from battle_factory import BattleFactory
from difficulty import Difficulty


class GameLoop:

    def __init__(self):
        self.difficulty = Difficulty(1)  # Default difficulty level

    def get_difficulty(self):
        return self.difficulty.value

    def set_difficulty(self, value):
        self.difficulty = Difficulty(value)

    # Start of the Game loop calling any battle and story events
    def start_game(self, player):
        current_difficulty = self.get_difficulty()
        print(f'Current Game Difficulty: {current_difficulty}')
        # Start tutorial battle
        self.start_tutorial_battle(player)

    def start_tutorial_battle(self, player):
        # Initialise multiple enemies
        enemy1 = MonsterFactory.create_basic_monster('wolf', self.difficulty)
        enemy2 = MonsterFactory.create_basic_monster('bear', self.difficulty)

        # Create a list of enemies
        enemies = [enemy1, enemy2]

        # Create and start the battle with the player and the list of enemies
        battle = BattleFactory.create_battle(player, enemies)
        battle.start_battle()

