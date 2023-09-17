import unittest
from number_in_interval import number_in_interval as nii


class TestEON(unittest.TestCase):
    def test_out_interval(self):
        self.assertFalse(nii(10), 'Это число в диапазоне от 25 до 100')
        self.assertFalse(nii(105), 'Это число в диапазоне от 25 до 100')

    def test_in_interval(self):
        self.assertTrue(nii(30), 'Это число не в диапазоне от 25 до 100')


