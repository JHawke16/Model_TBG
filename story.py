from party_member import PartyMember
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory


class Story:
    def __init__(self, player, game_loop):
        self.player = player
        self.game_loop = game_loop
        self.story_progress = 0

    def prologue(self):
        print("\nPrologue:")
        print("\nYour town was destroyed by an elder dragon, and you seek revenge.")
        print("You are currently on the outskirts of a forest when you hear a woman being attacked by monsters.")
        print('You rush over and see that she is being attacked by some monsters.')
        print('You ready your weapon and prepare for battle')
        self.story_progress = 1
        self.game_loop.start_tutorial_battle(self.player)

    def next_part(self):
        if self.story_progress == 1:
            print("\nAfter defeating the monsters, the woman thanks you and tells you that she is also an "
                  "adventurer and that she will join you on your quest against the dragon.")
            print("Her name is Claire and she joins your party!")
            # Create Claire and add her to the player's party
            claire = PartyMember(
                'Claire', 5, 2, 7,
                WeaponFactory.create_weapon('staff', 'basic'),
                SkillFactory.create_skills(['fireball', 'flames', 'magma', 'blaze'], 'basic')
            )
            self.player.add_party_member(claire)
            self.story_progress = 2

            # Start a new battle with Claire
            print("\nYou hear more monsters approaching, attracted by the noise of the battle.")
            print("You and Claire ready your weapons for another fight!")
            self.game_loop.start_battle_with_claire(self.player)
        elif self.story_progress >= 2:
            self.game_loop.start_random_battle(self.player)
        # Can add more parts of the story here

    def continue_story(self):
        if self.story_progress == 0:
            self.prologue()
        else:
            self.next_part()


