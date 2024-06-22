from random import choice


class Battle:
    def __init__(self, player, enemies, difficulty):
        self.player = player
        self.enemies = enemies if isinstance(enemies, list) else [enemies]
        self.difficulty = difficulty
        self.round_number = 0
        self.previous_player_action = None
        self.previous_enemy_action = None
        self.battle_log = []

    def start_battle(self):
        self.battle_flow()

    def get_action_order(self):
        combatants = [('player', self.player)] + [('enemy', enemy) for enemy in self.enemies]
        combatants.sort(key=lambda x: x[1].speed, reverse=True)
        return combatants

    def log_battle_data(self, combatant, action):
        data = {
            'round_number': self.round_number,
            'difficulty': self.difficulty.value,
            'player_health': self.player.health,
            'player_level': self.player.level,
            'player_action': self.previous_player_action,
            'player_energy': self.player.weapon.energy if self.player.weapon else None,
            'player_weapon_damage': self.player.weapon.damage if self.player.weapon else None,
            'player_weapon_defense': self.player.weapon.defense if self.player.weapon else None,
            'player_speed': self.player.speed,
            'enemy_health': combatant.health,
            'enemy_level': combatant.level,
            'enemy_action': self.previous_enemy_action,
            'enemy_energy': combatant.weapon.energy if combatant.weapon else None,
            'enemy_weapon_damage': combatant.weapon.damage if combatant.weapon else None,
            'enemy_weapon_defense': combatant.weapon.defense if combatant.weapon else None,
            'enemy_speed': combatant.speed,
            'action_taken': action
        }
        self.battle_log.append(data)

    def battle_flow(self):
        print("\n=======================")
        print("     Battle starts!    ")
        print("=======================")
        enemy_names = [enemy.name for enemy in self.enemies if enemy.check_alive()]
        print(f"\nEnemies entering the battle: {', '.join(enemy_names)}\n")

        while self.player.check_alive() and any(enemy.check_alive() for enemy in self.enemies):
            self.round_number += 1
            for combatant_type, combatant in self.get_action_order():
                if combatant_type == 'player' and combatant.check_alive():
                    action = self.player_action(combatant)
                    self.previous_player_action = action
                elif combatant_type == 'enemy' and combatant.check_alive():
                    action = self.enemy_action(combatant)
                    self.previous_enemy_action = action
                    self.log_battle_data(combatant, action)

                if not self.player.check_alive():
                    print("\n=======================")
                    print("    Battle Over. You were defeated.")
                    print("=======================")
                    self.log_battle_data(combatant, 'player_defeated')
                    return

            self.handle_defeated_enemies()

        print("\n=======================")
        print(" Battle Over. All enemies defeated!")
        print("=======================")
        self.player.reset_stats()

    def player_action(self, player):
        valid_action_taken = False
        action = None
        while not valid_action_taken:
            print('Choose an action:\n1. Attack\n2. Skills\n3. Defend\n4. Flee\n5. Use Item\n')
            p_choice = input('Choice: ')

            if p_choice in ['1', '2']:  # Attack or Skills
                target_enemy = self.select_enemy_target()
                if target_enemy:
                    if p_choice == '1':  # Attack
                        damage = player.attack()
                        target_enemy.take_damage(damage)
                        action = 'attack'
                        valid_action_taken = True

                    elif p_choice == '2':  # Skills
                        skill_damage = player.skill_attack()
                        if skill_damage is not None:
                            target_enemy.take_damage(skill_damage)
                            action = 'skill'
                            valid_action_taken = True

            elif p_choice == '3':  # Defend
                player.defend()
                action = 'defend'
                valid_action_taken = True
            elif p_choice == '4':  # Flee
                if player.flee():
                    action = 'flee'
                    return action  # End the battle if the player successfully flees
                action = 'flee'
                valid_action_taken = True
            elif p_choice == '5':  # Use Item
                if self.use_item():
                    action = 'use_item'
                    valid_action_taken = True

        return action

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
            print("Please enter a number.\n")
        return None

    def enemy_action(self, enemy):
        if self.player.check_alive():
            if enemy.health / enemy.max_health < 0.15:
                if enemy.flee():
                    self.enemies.remove(enemy)
                    return 'flee'

            action_choice = choice(['attack', 'skill_attack', 'defend'])
            action = None
            if action_choice == 'attack':
                damage = enemy.attack()
                self.player.take_damage(damage)
                action = 'attack'
            elif action_choice == 'skill_attack':
                skill_damage = enemy.skill_attack()
                self.player.take_damage(skill_damage)
                action = 'skill_attack'
            elif action_choice == 'defend':
                enemy.defend()
                action = 'defend'
            if not self.player.check_alive():
                print('Battle Over')
            return action

    def handle_defeated_enemies(self):
        for enemy in self.enemies:
            if not enemy.check_alive():
                gold_dropped = enemy.drop_gold()
                exp_dropped = enemy.drop_exp()
                self.player.gain_gold(gold_dropped)
                self.player.gain_exp(exp_dropped)
                dropped_item = enemy.drop_item()
                if dropped_item:
                    self.player.inventory.add_item(dropped_item)

        self.enemies = [enemy for enemy in self.enemies if enemy.check_alive()]

    def use_item(self):
        if self.player.inventory.is_empty():
            print("No items in inventory.")
            return False  # Return False to indicate no action was taken

        print("Choose an item to use:")
        self.player.inventory.display_items()

        item_choices = {i + 1: item for i, item in enumerate(self.player.inventory.items)}
        for number, item in item_choices.items():
            print(f"{number}. {item.name}")

        item_choice = input("Item number: ")
        try:
            item_choice = int(item_choice)
            if item_choice in item_choices:
                item_name = item_choices[item_choice].name
                if self.player.use_item(item_name):
                    print(f'\n{self.player.name} used {item_name}.')
                    print(f'{self.player.name} Health: {self.player.health}')
                    if self.player.weapon:
                        print(f'Energy Remaining: {self.player.weapon.energy}\n')
                    return True  # Return True to indicate an action was taken
                else:
                    print(f'Cannot use {item_name}.')
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
        return False  # Return False if no valid action was taken
