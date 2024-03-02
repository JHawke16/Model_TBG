class Menu:

    def main_menu(self):
        print('Welcome to TBG Alpha V 0.0002')
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
                from char_creation import CharCreation
                char_create = CharCreation()
                player = char_create.char_create()  # Capture the returned player object

                # After character creation, start the game loop
                from game_loop import GameLoop
                game_loop = GameLoop()
                game_loop.start_game(player)  # Pass the created player into the game loop
                correct = False