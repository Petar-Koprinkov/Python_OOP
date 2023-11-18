from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOOD = ["Meat"]
    GAINED_WEIGHT_PER_PIECE = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOOD = ["Meat", "Vegetable", "Fruit", "Seed"]
    GAINED_WEIGHT_PER_PIECE = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
