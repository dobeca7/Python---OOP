from unittest import TestCase, main

# from Forth_Car_Manager.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Audi", "A4", 10, 50)

    def test_correct_init(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("A4", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!",str(ex.exception))

    def test_model_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!",str(ex.exception))

    def test_fuel_consumption_with_0_consumption_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_0_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_expect_refueling_with_all_capacity(self):
        self.car.fuel_capacity = 45
        self.car.refuel(50)
        self.assertEqual(45,self.car.fuel_amount)

    def test_refuel_if_fuel_is_0(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!",str(ex.exception))

    def test_drive_with_enough_fuel_amount_expect_fuel_amount_decrease(self):
        self.car.fuel_amount = 50
        self.car.drive(10)
        self.assertEqual(49,self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_amount_raises_exception(self):
        self.car.fuel_amount = 1
        with self.assertRaises(Exception) as ex:
            self.car.drive(10000)

        self.assertEqual("You don't have enough fuel to drive!",str(ex.exception))

if __name__ == "__main__":
    main()