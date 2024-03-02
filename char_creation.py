from weapon_factory import WeaponFactory
from skill_factory import SkillFactory
from player import Player


class CharCreation:

    def char_create(self):
        print('\nWelcome to Character Creation')
        print('The class selected here only determines your starting stats as well as weapons and skills.'
              'You are able to make any build you like as you play')
        print('-----------------------------\n')
        print('Please select your starting class from the options below. Once you select an option you'
              'will receive more info it and then you can either confirm or make a new selection.\n')

        correct = True
        while correct:
            choice = input('\n1. Warrior\n2. Rogue\n3. Mage\n4. Commoner\nChoice: ')
            if choice == '1':
                print('\nWarrior stats:\nWeapon - Sword (Damage:10, Defense:4, Energy:3)\nSkills - Slash, Swing, Stab'
                      '\nHealth = 30'
                      '\nSpeed = 10'
                      )
                choice_w = input('\nWould you like to select the warrior? (y/n)\nChoice: ')
                if choice_w.lower() == 'y':
                    print('\nWarrior Selected!')
                    p_name = input('Please enter a name for your character\nName: ')
                    p_skills = SkillFactory.create_skills(['slash', 'swing', 'stab'])
                    p_weapon = WeaponFactory.create_weapon('sword')
                    player = Player(p_name, 15, 0, 1, 0, 5, p_weapon, p_skills)
                    print('\nStarting Tutorial Battle\n')
                    correct = False

        return player
