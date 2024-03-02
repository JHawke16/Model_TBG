from battle import Battle


class BattleFactory:

    @staticmethod
    def create_battle(player, enemy):
        return Battle(player, enemy)