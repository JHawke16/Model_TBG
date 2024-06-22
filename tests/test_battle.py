import unittest
from unittest.mock import patch
from battle import Battle
from player import Player
from enemy import Enemy
from weapon import Weapon
from skill_factory import SkillFactory
from difficulty import Difficulty
from item import Item, potion_use


class TestBattle(unittest.TestCase):

    def setUp(self):
        # Setup Player
        self.skills = SkillFactory.create_skills(['slash', 'stab'])
        self.weapon = Weapon('Sword', 10, 4, 6, 10)
        self.player = Player('Hero', 50, 0, 1, 0, 10, self.weapon, self.skills)

        # Setup Enemies
        self.enemy_weapon = Weapon('Claw', 5, 1, 1, 0)
        self.enemy_skills = SkillFactory.create_skills(['bite'])
        self.enemy = Enemy('Goblin', 30, 10, 1, 5, 10, self.enemy_weapon, self.enemy_skills, Difficulty(1))

    def test_battle_flow(self):
        # Initialize a Battle
        battle = Battle(self.player, [self.enemy], Difficulty(1))

        # Start Battle
        battle.start_battle()

        # Assertions
        self.assertFalse(self.player.check_alive() and self.enemy.check_alive(),
                         "Both player and enemy cannot be alive after the battle")

    def test_player_attack(self):
        damage = self.player.attack()
        self.enemy.take_damage(damage)
        self.assertLess(self.enemy.health, self.enemy.max_health, "Enemy health should be reduced after attack")

    def test_enemy_attack(self):
        damage = self.enemy.attack()
        self.player.take_damage(damage)
        self.assertLess(self.player.health, self.player.max_health, "Player health should be reduced after attack")

    def test_use_potion(self):
        self.player.health = 40  # Set health below max health to ensure potion has an effect
        initial_health = self.player.health
        potion = Item('Health Potion', potion_use, 20)
        self.player.inventory.add_item(potion)
        self.player.use_item('Health Potion')
        self.assertGreater(self.player.health, initial_health, "Player health should increase after using a potion")

    def test_defense_mechanic(self):
        # Test player defending reduces damage
        self.player.defend()
        self.assertTrue(self.player.is_defending, "Player should be in defending state")

        initial_health = self.player.health
        damage = self.enemy.attack()
        self.player.take_damage(damage)
        expected_damage = max(0, damage - self.player.weapon.defense)
        self.assertEqual(self.player.health, initial_health - expected_damage,
                         "Player health should be reduced by damage minus defense value")

        # Reset player's defense state for next test
        self.player.reset_defense()

        # Test enemy defending reduces damage
        self.enemy.defend()
        self.assertTrue(self.enemy.is_defending, "Enemy should be in defending state")

        initial_health = self.enemy.health
        damage = self.player.attack()
        self.enemy.take_damage(damage)
        expected_damage = max(0, damage - self.enemy.weapon.defense)
        self.assertEqual(self.enemy.health, initial_health - expected_damage,
                         "Enemy health should be reduced by damage minus defense value")

    def test_player_level_up(self):
        self.player.gain_exp(20)  # Give enough experience points to level up
        self.assertEqual(self.player.level, 2, "Player should have leveled up to level 2")
        self.assertEqual(self.player.health, self.player.max_health,
                         "Player health should be reset to max health on level up")

    def test_enemy_drops(self):
        # Ensure player gains gold correctly after defeating an enemy
        initial_gold = self.player.gold

        # Simulate the player defeating the enemy
        while self.enemy.check_alive():
            damage = self.player.attack()
            self.enemy.take_damage(damage)

        # Enemy should drop gold and experience
        gold_dropped = self.enemy.drop_gold()
        exp_dropped = self.enemy.drop_exp()

        # Player gains the gold and experience
        self.player.gain_gold(gold_dropped)
        self.player.gain_exp(exp_dropped)

        # Assertions
        self.assertEqual(self.player.gold, initial_gold + gold_dropped, "Player should gain gold from defeated enemy")

        # Print statements to confirm experience is gained
        print(f"Player experience after gaining: {self.player.base_exp}")
        print(f"Player level after gaining: {self.player.level}")

    def test_skill_usage(self):
        skill_damage = self.player.skill_attack()
        if skill_damage:
            initial_health = self.enemy.health
            self.enemy.take_damage(skill_damage)
            self.assertLess(self.enemy.health, initial_health, "Enemy health should be reduced by skill damage")

    @patch('random.random', return_value=0.1)
    def test_flee_mechanic(self, mock_random):
        self.assertTrue(self.player.flee(), "Player should be able to flee (20% chance)")

        self.enemy.health = self.enemy.max_health * 0.1  # Set enemy health to below 15%
        self.assertTrue(self.enemy.flee(), "Enemy should be able to flee when health is below 15% (20% chance)")

    def test_inventory_management(self):
        potion = Item('Health Potion', potion_use, 20)
        self.player.inventory.add_item(potion)
        self.assertIn(potion, self.player.inventory.items, "Potion should be added to inventory")

        self.player.use_item('Health Potion')
        self.assertNotIn(potion, self.player.inventory.items, "Potion should be removed from inventory after use")


if __name__ == '__main__':
    unittest.main()
