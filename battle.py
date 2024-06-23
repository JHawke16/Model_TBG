from random import choice
from party_member import PartyMember
from enemy import Enemy  # Make sure the Enemy class is imported


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
        combatants = [('player', self.player)] + [
            (f'party_{i}', member) for i, member in enumerate(self.player.party_members) if member.check_alive()
        ] + [('enemy', enemy) for enemy in self.enemies if enemy.check_alive()]
        combatants.sort(key=lambda x: x[1].speed, reverse=True)
        return combatants

    def log_battle_data(self, combatant, action):
        data = {
            'round_number': self.round_number,
            'combatant_name': combatant.name,
            'combatant_type': 'player' if combatant == self.player else 'enemy' if isinstance(combatant, Enemy) else 'party_member',
            'combatant_health': combatant.health,
            'combatant_energy': combatant.weapon.energy if combatant.weapon else None,
            'action_taken': action
        }
        self.battle_log.append(data)
        # print(f"Log: {data}")  # Print log for debugging

    def battle_flow(self):
        print("\n=======================")
        print("     Battle starts!    ")
        print("=======================")
        enemy_names = [enemy.name for enemy in self.enemies if enemy.check_alive()]
        print(f"\nEnemies entering the battle: {', '.join(enemy_names)}\n")

        while self.player.check_alive() and any(enemy.check_alive() for enemy in self.enemies):
            self.round_number += 1
            print(f"\n--- Round {self.round_number} ---")
            action_order = self.get_action_order()
            combatant = None

            for combatant_type, combatant in action_order:
                if combatant.check_alive():
                    if combatant_type == 'player':
                        action = self.player_action(combatant)
                        self.previous_player_action = action
                    elif 'party' in combatant_type:
                        action = self.party_member_action(combatant)
                        self.previous_player_action = action
                    elif combatant_type == 'enemy':
                        action = self.enemy_action(combatant)
                        self.previous_enemy_action = action
                        self.log_battle_data(combatant, action)

            self.handle_defeated_enemies()
            self.check_level_up()

            if not self.player.check_alive():
                print("\n=======================")
                print("    Battle Over. You were defeated.")
                print("=======================")
                self.log_battle_data(combatant, 'player_defeated')
                return

        print("\n=======================")
        print(" Battle Over. All enemies defeated!")
        print("=======================")
        self.player.reset_stats()
        for member in self.player.party_members:
            member.reset_stats()

    def player_action(self, player):
        valid_action_taken = False
        action = None
        while not valid_action_taken:
            print('Choose an action:\n1. Attack\n2. Skills\n3. Defend\n4. Flee\n5. Use Item\n')
            p_choice = input('Choice: ')

            if p_choice in ['1', '2']:
                target_enemy = self.select_enemy_target()
                if target_enemy:
                    if p_choice == '1':
                        print(f'\n{player.name} targets {target_enemy.name} with an attack.')
                        damage = player.attack()
                        target_enemy.take_damage(damage)
                        action = 'attack'
                        valid_action_taken = True

                    elif p_choice == '2':
                        print(f'\n{player.name} targets {target_enemy.name} with a skill attack.')
                        skill_damage = player.skill_attack()
                        if skill_damage is not None:
                            target_enemy.take_damage(skill_damage)
                            action = 'skill'
                            valid_action_taken = True

            elif p_choice == '3':
                player.defend()
                action = 'defend'
                valid_action_taken = True
            elif p_choice == '4':
                if player.flee():
                    action = 'flee'
                    return action
                action = 'flee'
                valid_action_taken = True
            elif p_choice == '5':
                if self.use_item():
                    action = 'use_item'
                    valid_action_taken = True

        return action

    def party_member_action(self, party_member):
        living_enemies = [enemy for enemy in self.enemies if enemy.check_alive()]
        if living_enemies:
            skills_with_matching_weapon = [skill for skill in party_member.skills if party_member.weapon.weapon_type in skill.required_weapon_types]
            if skills_with_matching_weapon:
                action_choice = choice(['skill_attack'] * 3 + ['attack'])  # Prioritize skill attack
            else:
                action_choice = 'attack'

            if action_choice == 'attack':
                target_enemy = choice(living_enemies)
                print(f'\n{party_member.name} targets {target_enemy.name} with an attack.')
                damage = party_member.attack()
                target_enemy.take_damage(damage)
                self.log_battle_data(party_member, 'attack')
                return 'attack'
            elif action_choice == 'skill_attack':
                target_enemy = choice(living_enemies)
                print(f'\n{party_member.name} targets {target_enemy.name} with a skill attack.')
                skill_damage = party_member.skill_attack()
                if skill_damage is not None:
                    target_enemy.take_damage(skill_damage)
                    self.log_battle_data(party_member, 'skill_attack')
                    return 'skill_attack'
        return 'none'

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
            target = choice([self.player] + [member for member in self.player.party_members if member.check_alive()])

            if action_choice == 'attack':
                print(f'\n{enemy.name} targets {target.name} with an attack.')
                damage = enemy.attack()
                target.take_damage(damage)
                action = 'attack'
            elif action_choice == 'skill_attack':
                print(f'\n{enemy.name} targets {target.name} with a skill attack.')
                skill_damage = enemy.skill_attack()
                target.take_damage(skill_damage)
                action = 'skill_attack'
            elif action_choice == 'defend' and enemy.speed > target.speed:
                enemy.defend()
                action = 'defend'
            if isinstance(target, PartyMember) and not target.check_alive():
                self.handle_party_member_knockout(target)
            self.log_battle_data(enemy, action)
            return action

    def handle_defeated_enemies(self):
        defeated_enemies = [enemy for enemy in self.enemies if not enemy.check_alive()]
        for enemy in defeated_enemies:
            gold_dropped = enemy.drop_gold()
            exp_dropped = enemy.drop_exp()
            self.player.gain_gold(gold_dropped)
            self.player.distribute_exp(exp_dropped)
            dropped_item = enemy.drop_item()
            if dropped_item:
                self.player.inventory.add_item(dropped_item)

        self.enemies = [enemy for enemy in self.enemies if enemy.check_alive()]

    def use_item(self):
        if self.player.inventory.is_empty():
            print("No items in inventory.")
            return False

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
                    return True
                else:
                    print(f'Cannot use {item_name}.')
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
        return False

    def handle_party_member_knockout(self, member):
        member.health = 0  # Ensure the health is 0
        print(f'{member.name} has been knocked out and cannot participate in the rest of the battle.')

    def check_level_up(self):
        self.player.level_up()
        for member in self.player.party_members:
            member.level_up()
