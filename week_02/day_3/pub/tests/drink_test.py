import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Whiskey Sour", 8.00, 2)
        
    def test_has_a_name(self):
        self.assertEqual("Whiskey Sour", self.drink.name)

    def test_has_a_price(self):
        self.assertEqual(8, self.drink.price)

    def test_has_alcohol_level(self):
        self.assertEqual(2, self.drink.alcohol_level)