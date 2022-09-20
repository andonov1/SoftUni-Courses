class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class CarTests(TestCase):

    def test_car_init(self):
        car = Car('Audi', 'A3', 7, 45)

        self.assertEqual('Audi', car.make)
        self.assertEqual('A3', car.model)
        self.assertEqual(7, car.fuel_consumption)
        self.assertEqual(45, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_make_invalid_value_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car(0, 'A3', 7, 45)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car('', 'A3', 7, 45)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_invalid_value_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Audi', 0, 7, 45)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car('Audi', '', 7, 45)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_invalid_value_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Audi', 'A3', 0, 45)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car('Audi', 'A3', -1, 45)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_invalid_value_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Audi', 'A3', 7, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car('Audi', 'A3', 7, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_invalid_value_raises(self):
        car = Car('Audi', 'A3', 7, 45)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_invalid_value_raises(self):
        car = Car('Audi', 'A3', 7, 45)

        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_working_correctly(self):
        car = Car('Audi', 'A3', 7, 45)

        car.refuel(5)
        self.assertEqual(5, car.fuel_amount)

        car.refuel(46)
        self.assertEqual(45, car.fuel_amount)

    def test_drive_invalid_value_raises(self):
        car = Car('Audi', 'A3', 7, 45)

        with self.assertRaises(Exception) as ex:
            car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_working_correctly(self):
        car = Car('Audi', 'A3', 7, 45)
        car.refuel(40)

        car.drive(5)
        result = car.fuel_amount - ((5 / 100) * car._Car__fuel_consumption)
        self.assertEqual(f'{result:.2f}', car.fuel_amount)


if __name__ == '__main__':
    main()
