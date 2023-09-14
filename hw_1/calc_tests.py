import unittest
from calculate_discount import calculate_discount as calc


class TestCalc(unittest.TestCase):
    def test_type_sum(self):
        self.assertRaises(TypeError, calc, 100)

    def test_type_pers(self):
        self.assertRaises(TypeError, calc, 100.4, '10')

    def test_value_sum(self):
        self.assertRaises(ValueError, calc, -100.4, 10)

    def test_value_pers(self):
        self.assertRaises(ValueError, calc, 100.4, 101)

    def test_well_done(self):
        self.assertEqual(calc(200.0, 10), 180.0)