from battle import Battle


class BattleFactory:

    @staticmethod
    def create_battle(player, enemies, difficulty):
        return Battle(player, enemies, difficulty)
