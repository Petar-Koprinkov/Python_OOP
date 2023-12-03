from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 85.50
    horse_power = 190.50
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_correct_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_typing(self):
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.horse_power, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)

    def test_failing_driving(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_successful_driving(self):
        self.vehicle.drive(10)
        self.assertEqual(73.0, self.vehicle.fuel)

    def test_refuel_failed(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_successfully(self):
        self.vehicle.fuel = 10.5
        self.vehicle.refuel(10)
        self.assertEqual(20.5, self.vehicle.fuel)

    def test_get_correct_string(self):
        self.assertEqual(f"The vehicle has {self.horse_power} "
                         f"horse power with {self.fuel} fuel left and "
                         f"{self.DEFAULT_FUEL_CONSUMPTION} fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()