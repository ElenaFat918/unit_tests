import unittest
from even_odd_number import even_odd_number as eon


class TestEON(unittest.TestCase):
    def test_odd_num(self):
        self.assertTrue(eon(5), 'Проверяемое число четное')

    def test_even_num(self):
        self.assertFalse(eon(6), 'Проверяемое число нечетное')
