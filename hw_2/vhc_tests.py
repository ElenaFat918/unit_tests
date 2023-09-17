import unittest
from vehicle import Vehicle as Vhc
from car import Car
from bike import Bike


class TestVhc(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Toyota', 'Model AA', 1936, 4)
        self.bike = Bike('American Chopper', 'Bike Billy', 1950, 2)

    def test_class_car(self):
        self.assertIsInstance(self.car, Vhc, 'Не является наследником класса')

    def test_class_bike(self):
        self.assertIsInstance(self.bike, Vhc, 'Не является наследником класса')

    def test_wheels(self):
        self.assertEqual(self.car.count_wheels, 4, 'Объект Car создается не с 4-мя колесами!')
        self.assertEqual(self.bike.count_wheels, 2, 'Объект Bike создается не с 2-мя колесами!')

    def test_speed(self):
        self.car.test_drive()
        self.bike.test_drive()
        self.assertEqual(self.car.get_speed, 60, 'Объект Car не соответствует скорости 60 км/ч!')
        self.assertEqual(self.bike.get_speed, 75, 'Объект Bike не соответствует скорости 75 км/ч!')

    def test_park(self):
        self.car.test_drive()
        self.car.park()
        self.bike.test_drive()
        self.bike.park()
        self.assertEqual(self.car.get_speed, 0, 'Объект Car не остановился')
        self.assertEqual(self.bike.get_speed, 0, 'Объект Bike не остановился')
