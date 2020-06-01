import unittest
import random
from python_loops import *


class TestLoops(unittest.TestCase):
    def test_check_tea_temp_too_cold(self):
        self.assertEqual(check_tea_temp(20), "Tea is too cold!")

    def test_check_tea_already_normal(self):
        self.assertEqual(check_tea_temp(50), "Tea is ready to be drunk!")

    def test_random_tea_too_cold(self):
        self.assertEqual(check_tea_temp(random.randint(0, 49)), "Tea is too cold!")

    def test_random_tea_already_normal(self):
        self.assertEqual(check_tea_temp(random.randint(50, 90)), "Tea is ready to be drunk!")

    def test_sort_teas_no_teas_cold_enough(self):
        teas = [20, 30, 50, 40, 60, 80]
        self.assertEqual(sort_drinkable_teas(teas, 10), "No teas were cold enough")

    def test_sort_teas_one_match(self):
        teas = [20, 30, 50, 40, 60, 80]
        self.assertEqual(sort_drinkable_teas(teas, 20), [20])

    def test_sort_teas_all_match(self):
        teas = [20, 30, 50, 40, 60, 80]
        self.assertEqual(sort_drinkable_teas(teas, 80), teas)

    def test_sort_teas_random_no_match(self):
        teas = [20, 30, 50, 40, 60, 80]
        self.assertEqual(sort_drinkable_teas(teas, random.randint(0, 10)), "No teas were cold enough")

if __name__ == '__main__':
    unittest.main()
