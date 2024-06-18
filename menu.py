class Menu:

    def main_menu(self):
        # Version control for every time code is pushed
        print('Welcome to TBG Alpha Version 0.004')
        print('----------------------------------\n')
        correct = True
        while correct:
            print('----------')
            print('Main Menu')
            print('----------\n')
            choice = input(
                'Please select an option below (Enter the number value to make your choice)'
                '\n1. New Game'
                '\n2. Load Game'
                '\n3. Information'
                '\n4. Exit'
                '\nChoice: '
            )
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
                print('\nLoading Saved Game')

            elif choice == '3':
                print('\nInfo about the Game')

            elif choice == '4':
                print('\nExiting Game')
                exit()
