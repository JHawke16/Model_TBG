from monster_factory import MonsterFactory
from battle_factory import BattleFactory
from difficulty import Difficulty
from random import randint
from game_menu import GameMenu


class GameLoop:

    def __init__(self):
        self.difficulty = Difficulty(1)  # Default difficulty level

    def get_difficulty(self):
        return self.difficulty.value

    def set_difficulty(self, value):
        self.difficulty = Difficulty(value)

    def start_game(self, player):
        current_difficulty = self.get_difficulty()
        print(f'Current Game Difficulty: {current_difficulty}')
        # Start tutorial battle first
        self.start_tutorial_battle(player)
        # Show the in-game menu after the tutorial battle
        self.show_game_menu(player)

    def start_tutorial_battle(self, player):
        num_enemies = randint(2, 4)
        enemies = MonsterFactory.create_random_monsters(num_enemies, self.difficulty)
        battle = BattleFactory.create_battle(player, enemies, self.difficulty)
        battle.start_battle()

    def show_game_menu(self, player):
        game_menu = GameMenu(player, self)
        while True:
            action = game_menu.display_menu()
            if action == 'continue':
                self.start_tutorial_battle(player)
            elif action == 'save':
                game_menu.save_game()
            elif action == 'view_items':
                game_menu.view_items()
            elif action == 'view_stats':
                game_menu.view_stats()
            elif action == 'view_quests':
                game_menu.view_quests()
            elif action == 'change_difficulty':
                game_menu.change_difficulty()
            elif action == 'exit':
                game_menu.exit_game()
