from unittest import TestCase
from project.hero import Hero


class TestHero(TestCase):
    username = "Petar"
    health = 50.50
    damage = 10.10
    level = 23

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_correct_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)
        self.assertEqual(self.level, self.hero.level)

    def test_correct_typing(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.damage, float)

    def test_battle_when_enemy_has_the_same_name_as_hero(self):
        self.enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_equal_or_under_zero(self):
        self.enemy = Hero("Gosho", self.level, 100, self.damage)
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health -= 1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_health_equal_or_under_zero(self):
        self.enemy = Hero("Gosho", self.level, 100, self.damage)
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

        self.enemy.health -= 1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_both_have_no_health_draw(self):
        self.enemy = Hero("Gosho", self.level, self.health, self.damage)
        self.hero.health = 10.10
        self.enemy.health = 10.10

        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.damage, self.hero.damage)
        self.assertEqual(-222.2, self.hero.health)

    def test_hero_won(self):
        self.enemy = Hero("Gosho", 1, 1, 1)
        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(24, self.hero.level)
        self.assertEqual(54.5, self.hero.health)
        self.assertEqual(15.1, self.hero.damage)

    def test_hero_lost(self):
        self.enemy = Hero("Gosho", 1000, 1000, 1000)
        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(1001, self.enemy.level)
        self.assertEqual(772.7, self.enemy.health)
        self.assertEqual(1005, self.enemy.damage)

    def test_return_string(self):
        result = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

        self.assertEqual(self.hero.__str__(), result)





