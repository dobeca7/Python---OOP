from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 100)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(100 , self.vehicle.fuel)
        self.assertEqual(100 , self.vehicle.horse_power)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION,self.vehicle.fuel_consumption)

    def test_drive_expect_fuel_decrease(self):
        self.vehicle.drive(10)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_drive_with_less_fuel_expect_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))


    def test_refuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)
        self.assertEqual(10, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception) )

    def test_string_representation(self):
        expected_result = f"The vehicle has 100 " \
               f"horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, str(self.vehicle))


if __name__ == "__main__":
    main()