class Menu:

    def main_menu(self):
        # Version control for every time code is pushed
        print('===================================')
        print('     Welcome to TBG Alpha Version 0.0005')
        print('===================================\n')

        correct = True
        while correct:
            print('=======================')
            print('        Main Menu      ')
            print('=======================\n')
            print('1. New Game')
            print('2. Load Game')
            print('3. Information')
            print('4. Exit\n')

            choice = input('Please select an option (Enter the number value): ')
            print('-----------------------')

            if choice == '1':
                print('\nStarting New Game - Moving to Character Creation\n')
                # import placed here to fix circular import errors
                from char_creation import CharCreation
                char_create = CharCreation()
                player = char_create.char_create()  # Capture the returned player object

                # After character creation, start the game loop
                from game_loop import GameLoop
                game_loop = GameLoop()
                game_loop.start_game(player)  # Pass the created player into the game loop
                correct = False

            elif choice == '2':
                print('\nLoading Saved Game\n')
                # Placeholder for load game functionality
                print('Feature not implemented yet.')

            elif choice == '3':
                print('\nGame Information\n')

            elif choice == '4':
                print('\nExiting Game\n')
                exit()

            else:
                print('\nInvalid choice, please select a valid option.\n')
