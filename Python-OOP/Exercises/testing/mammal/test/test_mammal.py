from unittest import TestCase, main

from Exercises.testing.mammal.project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal('name', 'mammal_type', 'sound')

    def test_init(self):
        mammal = Mammal('name', 'mammal_type', 'sound')
        self.assertEqual('name', mammal.name)
        self.assertEqual('mammal_type', mammal.type)
        self.assertEqual('sound', mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual(self.mammal._Mammal__kingdom, self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == "__main__":
    main()
