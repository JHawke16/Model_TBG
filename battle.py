class Battle:

    def __init__(self, player, enemies):
        self.player = player
        # Ensure enemies is a list for consistency
        self.enemies = enemies if isinstance(enemies, list) else [enemies]

    def get_action_order(self):
        # Create a list of all combatants and sort them by speed
        combatants = [('player', self.player)] + [('enemy', enemy) for enemy in self.enemies]
        combatants.sort(key=lambda x: x[1].speed, reverse=True)
        return combatants

    def battle_flow(self):
        print("\nBattle starts!")
        # Print the names of the enemies at the start of the battle
        enemy_names = [enemy.name for enemy in self.enemies if enemy.check_alive()]
        print(f"\nEnemies entering the battle: {', '.join(enemy_names)}")

        while self.player.check_alive() and any(enemy.check_alive() for enemy in self.enemies):
            for combatant_type, combatant in self.get_action_order():
                if combatant_type == 'player' and combatant.check_alive():
                    self.player_action(combatant)
                elif combatant_type == 'enemy' and combatant.check_alive():
                    self.enemy_action(combatant)

                # Break out of the loop if the player dies
                if not self.player.check_alive():
                    print('Battle Over. You were defeated.')
                    return

            # Remove defeated enemies from the list
            self.enemies = [enemy for enemy in self.enemies if enemy.check_alive()]

        print('Battle Over. All enemies defeated!')

    def player_action(self, player):
        valid_action_taken = False
        while not valid_action_taken:
            print('\nChoose an action:\n1. Attack\n2. Skills\n3. Defend\n4. Flee\n')
            p_choice = input('Choice: ')

            if p_choice in ['1', '2']:  # Attack or Skills
                target_enemy = self.select_enemy_target()
                if target_enemy:
                    if p_choice == '1':  # Attack
                        damage = player.attack()
                        target_enemy.take_damage(damage)
                        valid_action_taken = True

                    elif p_choice == '2':  # Skills
                        skill_damage = player.skill_attack()
                        if skill_damage is not None:  # Ensure skill was selected
                            target_enemy.take_damage(skill_damage)
                            valid_action_taken = True

            elif p_choice == '3':
                print('Defend action to be added')
                valid_action_taken = True  # Assuming defend action is always valid
            elif p_choice == '4':
                print('Flee action to be added')
                valid_action_taken = True  # Assuming flee action is always valid

    def select_enemy_target(self):
        print("\nChoose your target:")
        for i, enemy in enumerate([e for e in self.enemies if e.check_alive()], start=1):
            print(f"{i}. {enemy.name} (Health: {enemy.health})")
        target_choice = input("Target number: ")
        try:
            target_index = int(target_choice) - 1
            if 0 <= target_index < len(self.enemies) and self.enemies[target_index].check_alive():
                return self.enemies[target_index]
            else:
                print("Invalid target. Please select a valid enemy.")
        except ValueError:
            print("Please enter a number.")
        return None

    def enemy_action(self, enemy):
        if self.player.check_alive():
            damage = enemy.attack()
            self.player.take_damage(damage)
            if not self.player.check_alive():
                print('Battle Over')

    def start_battle(self):
        self.battle_flow()
