from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = ["Vegetable", "Fruit"]
    GAINED_WEIGHT_PER_PIECE = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOOD = ["Meat"]
    GAINED_WEIGHT_PER_PIECE = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOOD = ["Meat", "Vegetable"]
    GAINED_WEIGHT_PER_PIECE = 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOOD = ["Meat"]
    GAINED_WEIGHT_PER_PIECE = 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"

