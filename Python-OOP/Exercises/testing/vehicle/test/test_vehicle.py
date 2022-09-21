from unittest import TestCase, main

from Exercises.testing.vehicle.project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(30, 100)

    def test_init(self):
        fuel = 30
        horse_power = 100
        vehicle = Vehicle(fuel, horse_power)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(vehicle.fuel, vehicle.capacity)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test_str_return_proper_str(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
                          f"horse power with {self.vehicle.fuel} fuel left " \
                          f"and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected_result, str(self.vehicle))

    def test_drive_invalid_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_reduces_fuel_when_valid(self):
        distance = 10
        burned_fuel = distance * self.vehicle.fuel_consumption
        expected = self.vehicle.fuel - burned_fuel
        self.vehicle.drive(distance)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_refuel_invalid_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increases_fuel_when_valid(self):
        self.vehicle.capacity = 100

        self.vehicle.refuel(70)

        self.assertEqual(100, self.vehicle.fuel)


if __name__ == "__main__":
    main()
