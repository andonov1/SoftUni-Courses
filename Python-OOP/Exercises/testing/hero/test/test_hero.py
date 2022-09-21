from unittest import TestCase, main

from Exercises.testing.hero.project.hero import Hero


class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero('test', 5, 100, 25)
        self.enemy = Hero('enemy_test', 5, 100, 25)

    def test_init(self):
        hero = Hero('test', 1, 100, 20)

        self.assertEqual('test', hero.username)
        self.assertEqual(1, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(20, hero.damage)

    def test_battle_against_same_name_enemy(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_invalid__health(self):
        for health in [0, -1]:
            self.hero.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_invalid_enemy__health(self):
        for health in [0, -1]:
            self.enemy.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_returns_draw_when_both_heroes_die(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual('Draw', result)
        self.assertEqual(-25, self.hero.health)
        self.assertEqual(-25, self.enemy.health)

    def test_battle_hero_levels_up_after_win(self):
        enemy = Hero('enemy_test', 1, 100, 50)

        result = self.hero.battle(enemy)

        self.assertEqual('You win', result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(30, self.hero.damage)

    def test_battle_enemy_hero_levels_up_after_win(self):
        hero = Hero('test', 1, 100, 50)

        result = hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(6, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(30, self.enemy.damage)

    def test_str_correct(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_result, str(self.hero))


if __name__ == "__main__":
    main()