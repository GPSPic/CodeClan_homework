import unittest
from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 3)

# test 1
    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)

# test 2
    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink.name)