from monster_factory import MonsterFactory
from battle_factory import BattleFactory
from difficulty import Difficulty
from random import randint


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
        # Initialize a random number of enemies
        num_enemies = randint(2, 4)
        enemies = MonsterFactory.create_random_monsters(num_enemies, self.difficulty)

        # Creating and starting the battle with the player and the list of enemies
        battle = BattleFactory.create_battle(player, enemies, self.difficulty)
        battle.start_battle()
