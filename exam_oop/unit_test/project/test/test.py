from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Test Station")

    def test_init(self):
        self.assertEqual("Test Station", self.station.name)

    def test_station_name(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Ab"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.station.name = "Abc"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("Train A")
        self.assertEqual(len(self.station.arrival_trains), 1)
        self.assertEqual(self.station.arrival_trains[0], "Train A")

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("Train A")

        result = self.station.train_has_arrived("Train B")
        self.assertEqual(result, "There are other trains to arrive before Train B.")

        result = self.station.train_has_arrived("Train A")
        self.assertEqual(result, "Train A is on the platform and will leave in 5 minutes.")
        self.assertEqual(len(self.station.arrival_trains), 0)
        self.assertEqual(len(self.station.departure_trains), 1)
        self.assertEqual(self.station.departure_trains[0], "Train A")

    def test_train_has_left(self):
        self.assertFalse(self.station.train_has_left("Train A"))

        self.station.new_arrival_on_board("Train A")
        self.station.train_has_arrived("Train A")

        self.assertTrue(self.station.train_has_left("Train A"))
        self.assertEqual(len(self.station.departure_trains), 0)


if __name__ == '__main__':
    main()
