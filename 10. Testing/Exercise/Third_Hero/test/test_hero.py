from unittest import TestCase, main
from project.hero import Hero

class Test_Hero(TestCase):

    def setUp(self):
        self.hero = Hero("Dob", 1000, 100, 500)
        self.enemy = Hero("Joro", 1, 1, 1)

    def test_correct__init__(self):
        self.assertEqual("Dob", self.hero.username)
        self.assertEqual(1000, self.hero.level)
        self.assertEqual(500, self.hero.damage)
        self.assertEqual(100, self.hero.health)

    def test_battle_with_identical_usernames(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_with_zero_health_raises_value_error(self):
        self.hero.health = 0  # Arrange
        expected_string = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)  # Act

        self.assertEqual(expected_string, str(ve.exception))

    def test_battle_enemy_with_zero_health_raises_value_error(self):
        self.enemy.health = 0  # Arrange
        expected_string = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)  # Act

        self.assertEqual(expected_string, str(ve.exception))

    def test_battle_returning_draw(self):
        self.enemy.damage = 100
        self.enemy.level = 50

        self.assertEqual("Draw", self.hero.battle(self.enemy))
        self.assertEqual(-4900, self.hero.health)
        self.assertEqual(-499999, self.enemy.health)

    def test_battle_returning_win(self):

        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage + 5
        expected_damage = self.hero.damage + 5
        expected_result = self.hero.battle(self.enemy)

        self.assertEqual("You win", expected_result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle_returning_lost(self):
        self.hero, self.enemy = self.enemy, self.hero
        expected_enemy_level = self.enemy.level +1
        expected_enemy_health = self.enemy.health- self.hero.damage +5
        expected_enemy_damage = self.enemy.damage +5
        expected_result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", expected_result)
        self.assertEqual(expected_enemy_health, self.enemy.health)
        self.assertEqual(expected_enemy_level, self.enemy.level)
        self.assertEqual(expected_enemy_damage, self.enemy.damage)

    def test_correct__str__(self):
        expected_string = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_string, str(self.hero))

if __name__ == "__main__":
    main()