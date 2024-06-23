from monster_factory import MonsterFactory
from battle_factory import BattleFactory
from difficulty import Difficulty
from random import randint
from game_menu import GameMenu
from story import Story
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory
from party_member import PartyMember


class GameLoop:

    def __init__(self):
        self.difficulty = Difficulty(1)  # Default difficulty level
        self.story = None  # Initialize the story attribute

    def get_difficulty(self):
        return self.difficulty.value

    def set_difficulty(self, value):
        self.difficulty = Difficulty(value)

    def start_game(self, player):
        current_difficulty = self.get_difficulty()
        print(f'Current Game Difficulty: {current_difficulty}')
        # Start the story
        self.story = Story(player, self)
        self.story.continue_story()

    def start_tutorial_battle(self, player):
        # Initialize a random number of enemies
        num_enemies = randint(2, 3)
        enemies = MonsterFactory.create_random_monsters(num_enemies, player.level, 'basic', self.difficulty)

        # Creating and starting the battle with the player and the list of enemies
        battle = BattleFactory.create_battle(player, enemies, self.difficulty)
        battle.start_battle()

        # After the battle, show the in-game menu
        self.show_game_menu(player)

    def start_battle_with_claire(self, player):
        # Initialize a random number of enemies for the tutorial fight with Claire
        num_enemies = randint(3, 4)
        enemies = MonsterFactory.create_random_monsters(num_enemies, player.level, 'basic', self.difficulty)

        # Creating and starting the battle with the player, Claire, and the list of enemies
        battle = BattleFactory.create_battle(player, enemies, self.difficulty)
        battle.start_battle()

        # After the battle, show the in-game menu
        self.show_game_menu(player)

    def start_random_battle(self, player):
        # Initialize a random number of enemies for a random battle
        num_enemies = randint(2, 4)
        enemies = MonsterFactory.create_random_monsters(num_enemies, player.level, 'basic', self.difficulty)

        # Creating and starting the battle with the player and the list of enemies
        battle = BattleFactory.create_battle(player, enemies, self.difficulty)
        battle.start_battle()

        # After the battle, show the in-game menu
        self.show_game_menu(player)

    def show_game_menu(self, player):
        game_menu = GameMenu(player, self)
        while True:
            action = game_menu.display_menu()
            if action == 'continue':
                self.story.continue_story()
            elif action == 'save':
                game_menu.save_game()
            elif action == 'view_items':
                game_menu.view_items()
            elif action == 'view_stats':
                game_menu.view_stats()
            elif action == 'view_party_members':
                game_menu.view_party_members()
            elif action == 'view_quests':
                game_menu.view_quests()
            elif action == 'change_difficulty':
                game_menu.change_difficulty()
            elif action == 'exit':
                game_menu.exit_game()
