class Battle:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def determine_first_strike(self):
        if self.player.speed > self.enemy.speed:
            return "player"
        else:
            return "enemy"

    def battle_flow(self):
        first_strike = self.determine_first_strike()
        print(f"\n{first_strike.capitalize()} strikes first.")

        while self.player.check_alive() and self.enemy.check_alive():

            if first_strike == "player":
                self.enemy.take_damage(self.player.attack())
                if not self.enemy.check_alive():
                    print('Enemy Defeated')
                    exp = self.enemy.drop_exp()
                    self.player.gain_exp(exp)
                    break  # Exit the loop if the enemy is defeated

                first_strike = "enemy"  # Switch turns

            if first_strike == "enemy":
                self.player.take_damage(self.enemy.attack())
                if not self.player.check_alive():
                    print('Battle Over')
                    break  # Exit the loop if the player is defeated

                first_strike = "player"  # Switch turns

    def start_battle(self):
        self.battle_flow()
