import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("John Lennon", 10, 20)
        self.customer2 = Customer("Ringo", 4, 16)
        self.drink = {
            "drink": Drink("Beer", 4, 3),
        }
        self.food = Food("Chips", 3, 2)

    def test_customer_has_name(self):
        self.assertEqual("John Lennon", self.customer1.name)
        
    def test_increase_drunkeness(self):
        self.customer1.drink_the_drink(self.drink)
        self.assertEqual(3, self.customer1._drunkeness)

    def test_rejuvenation_via_food(self):
        self.customer1.drink_the_drink(self.drink)
        self.customer1.eat_the_food(self.food)
        self.assertEqual(1, self.customer1._drunkeness)

    # def test_reduce_wallet(self):
    #     self.customer1.reduce_wallet(10)
    #     self.customer2.reduce_wallet(10)
    #     self.assertEqual(0, self.customer1.get_wallet())
    #     self.assertEqual("No service", self.customer2.get_wallet())

    # def test_can_pay_for_drink__true(self):
    #     enough_money = self.customer1.can_pay_for_drink(10)
    #     self.assertTrue(enough_money)

    # def test_can_pay_for_drink__false(self):
    #     enough_money = self.customer1.can_pay_for_drink(10)
    #     self.assertFalse(enough_money)

 
