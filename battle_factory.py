from battle import Battle


class BattleFactory:

    @staticmethod
    def create_battle(player, enemies):
        # Battle is created with a list of enemies
        return Battle(player, enemies)
