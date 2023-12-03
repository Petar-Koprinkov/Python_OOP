from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    name = "Petar"
    type = "Human"
    sound = "speaking"
    __kingdom = "animals"

    def setUp(self) -> None:
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_correct_init(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual(self.__kingdom, self.mammal._Mammal__kingdom)

    def test_making_correct_sound(self):
        expected = f"{self.name} makes {self.sound}"
        self.assertEqual(expected, self.mammal.make_sound())

    def test_get_kingdom(self):
        expected = self.__kingdom
        self.assertEqual(expected, self.mammal.get_kingdom())

    def test_get_correct_info(self):
        expected = f"{self.name} is of type {self.type}"
        self.assertEqual(expected, self.mammal.info())


if __name__ == "__main__":
    main()
