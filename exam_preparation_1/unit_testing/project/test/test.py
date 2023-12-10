from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip1 = Trip(10_000, 1, False)
        self.trip2 = Trip(10_000, 2, False)
        self.trip3 = Trip(10_000, 2, True)

    def test_correct_init(self):
        self.assertEqual(10_000, self.trip1.budget)
        self.assertEqual(1, self.trip1.travelers)
        self.assertEqual(False, self.trip1.is_family)

    def test_setter_travelers(self):
        with self.assertRaises(ValueError) as ve:
            self.trip1.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_setter_is_family(self):
        self.assertTrue(self.trip3.is_family)

        self.trip1.is_family = True
        self.assertFalse(self.trip1.is_family)

    def test_destination_not_in_trip(self):
        result = self.trip1.book_a_trip("Serbia")
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_not_enough_money(self):
        result = self.trip2.book_a_trip("New Zealand")
        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_with_enough_money(self):
        result = self.trip2.book_a_trip("Bulgaria")
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 9000.00', result)
        self.assertEqual(9000, self.trip2.budget)
        self.assertEqual({"Bulgaria": 1000}, self.trip2.booked_destinations_paid_amounts)

        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 9100.00", self.trip3.book_a_trip("Bulgaria"))
        self.assertEqual(9100, self.trip3.budget)
        self.assertEqual({"Bulgaria": 900}, self.trip3.booked_destinations_paid_amounts)

    def test_booking_status_failed(self):
        result = self.trip1.booking_status()
        self.assertEqual(f'No bookings yet. Budget: 10000.00', result)

    def test_booking_status_successful(self):
        self.trip2.budget = 100_000_000
        self.trip2.book_a_trip("New Zealand")
        self.trip2.book_a_trip("Australia")
        self.trip2.book_a_trip("Brazil")

        result = "Booked Destination: Australia\n" \
                 "Paid Amount: 11400.00\n" \
                 "Booked Destination: Brazil\n" \
                 "Paid Amount: 12400.00\n" \
                 "Booked Destination: New Zealand\n" \
                 "Paid Amount: 15000.00\n" \
                 "Number of Travelers: 2\n" \
                 "Budget Left: 99961200.00"

        self.assertEqual(result, self.trip2.booking_status())


if __name__ == "__main__":
    main()
