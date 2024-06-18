from random import choice
import random


class Battle:

    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies if isinstance(enemies, list) else [enemies]

    def get_action_order(self):
        combatants = [('player', self.player)] + [('enemy', enemy) for enemy in self.enemies]
        combatants.sort(key=lambda x: x[1].speed, reverse=True)
        return combatants

    def battle_flow(self):
        print("\n=======================")
        print("     Battle starts!    ")
        print("=======================")
        enemy_names = [enemy.name for enemy in self.enemies if enemy.check_alive()]
        print(f"\nEnemies entering the battle: {', '.join(enemy_names)}\n")

        while self.player.check_alive() and any(enemy.check_alive() for enemy in self.enemies):
            for combatant_type, combatant in self.get_action_order():
                if combatant_type == 'player' and combatant.check_alive():
                    self.player_action(combatant)
                elif combatant_type == 'enemy' and combatant.check_alive():
                    self.enemy_action(combatant)

                if not self.player.check_alive():
                    print("\n=======================")
                    print("    Battle Over. You were defeated.")
                    print("=======================")
                    return

            self.handle_defeated_enemies()

        print("\n=======================")
        print(" Battle Over. All enemies defeated!")
        print("=======================")
        self.player.reset_stats()

    def player_action(self, player):
        valid_action_taken = False
        while not valid_action_taken:
            print('Choose an action:\n1. Attack\n2. Skills\n3. Defend\n4. Flee\n')
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
                        if skill_damage is not None:
                            target_enemy.take_damage(skill_damage)
                            valid_action_taken = True

            elif p_choice == '3':  # Defend
                player.defend()
                valid_action_taken = True
            elif p_choice == '4':  # Flee
                if player.flee():
                    return  # End the battle if the player successfully flees
                valid_action_taken = True

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
            if enemy.health / enemy.max_health < 0.15 and random.random() < 0.2:  # 15% health and 20% flee chance
                if enemy.flee():
                    self.enemies.remove(enemy)
                    return

            action_choice = choice(['attack', 'skill_attack', 'defend'])
            if action_choice == 'attack':
                damage = enemy.attack()
                self.player.take_damage(damage)
            elif action_choice == 'skill_attack':
                skill_damage = enemy.skill_attack()
                self.player.take_damage(skill_damage)
            elif action_choice == 'defend':
                enemy.defend()
            if not self.player.check_alive():
                print('Battle Over')

    def handle_defeated_enemies(self):
        for enemy in self.enemies:
            if not enemy.check_alive():
                gold_dropped = enemy.drop_gold()
                exp_dropped = enemy.drop_exp()
                self.player.gain_gold(gold_dropped)
                self.player.gain_exp(exp_dropped)

        self.enemies = [enemy for enemy in self.enemies if enemy.check_alive()]

    def start_battle(self):
        self.battle_flow()
