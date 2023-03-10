import unittest
from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 3)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)