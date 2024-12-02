from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Doncho", "tiger", "RAW")

    def test_correct_init(self):
        self.assertEqual("Doncho", self.mammal.name)
        self.assertEqual("tiger", self.mammal.type)
        self.assertEqual("RAW", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Doncho makes RAW", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Doncho is of type tiger", self.mammal.info())


if __name__ == "__main__":
    main()