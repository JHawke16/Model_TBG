class GameMenu:
    def __init__(self, player, game_loop):
        self.player = player
        self.game_loop = game_loop

    def display_menu(self):
        while True:
            print("\nIn-Game Menu:")
            print("1. Continue (Start New Battle)")
            print("2. Save Game")
            print("3. View Items")
            print("4. View Stats")
            print("5. View Party Members")
            print("6. View Quests")
            print("7. Change Difficulty")
            print("8. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                return 'continue'
            elif choice == '2':
                return 'save'
            elif choice == '3':
                return 'view_items'
            elif choice == '4':
                return 'view_stats'
            elif choice == '5':
                return 'view_party_members'
            elif choice == '6':
                return 'view_quests'
            elif choice == '7':
                return 'change_difficulty'
            elif choice == '8':
                return 'exit'
            else:
                print("Invalid choice. Please select a valid option.")

    def save_game(self):
        print("\nSaving game... (Not implemented yet)")

    def view_items(self):
        print("\nViewing items:")
        self.player.inventory.display_items()

    def view_stats(self):
        print("\nViewing stats:")
        print(f"Name: {self.player.name}")
        print(f"Health: {self.player.health}/{self.player.max_health}")
        print(f"Level: {self.player.level}")
        print(f"Exp: {self.player.base_exp}")
        print(f"Exp to next level: {self.player.required_exp - self.player.base_exp}")
        print(f"Gold: {self.player.gold}")
        print(f"Speed: {self.player.speed}")
        if self.player.weapon:
            print(f"Weapon: {self.player.weapon.name} (Damage: {self.player.weapon.damage}, Defense: {self.player.weapon.defense}, Energy: {self.player.weapon.energy}/{self.player.weapon.max_energy})")
        if self.player.skills:
            print("Skills:")
            for skill in self.player.skills:
                print(f"  - {skill.name} (Damage: {skill.damage}, Energy Cost: {skill.energy})")

    def view_party_members(self):
        print("\nViewing party members:")
        self.player.view_party_members()

    def view_quests(self):
        print("\nViewing quests... (Not implemented yet)")

    def change_difficulty(self):
        print("\nCurrent difficulty level:", self.game_loop.get_difficulty())
        try:
            new_difficulty = int(input("Enter new difficulty level: "))
            self.game_loop.set_difficulty(new_difficulty)
            print(f"Difficulty level changed to {new_difficulty}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def exit_game(self):
        print("\nExiting game")
        exit()
