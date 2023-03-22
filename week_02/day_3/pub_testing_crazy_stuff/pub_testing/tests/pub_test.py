import unittest
from src.pub import Pub
from src.drink import Drink
from src.food import Food
from src.customer import Customer


class TestPub(unittest.TestCase):
    pass
    def setUp(self):
        # self.drink1 = Drink("Whiskey Sour", 8.0, 2)
        # self.drink2 = Drink("Beer", 4.0, 3)
        # self.drink3 = Drink("Wine", 6.0, 1)
        drinks_menu = {
            "drink1": Drink("Whiskey Sour", 8.0, 2),
            "drink2": Drink("Beer", 4.0, 3),
            "drink3": Drink("Wine", 6.0, 1),
            }
        self.food1 = Food("Chips", 3, 2)
        self.food2 = Food("Humus", 4, 1)
        food_menu = [self.food1, self.food2]
        stock = {
            drinks_menu["drink1"]: 2,
            drinks_menu["drink2"]: 3,
            drinks_menu["drink3"]: 3,
            }
        self.pub = Pub("The Drunken Sailor", 0, drinks_menu, food_menu, stock)
        self.customer1 = Customer("John Lennon", 6, 20)
        self.customer2 = Customer("Ringo", 4, 16)
        self.customer3 = Customer("Paul McCartney", 50, 70)

    def test_add_to_till(self):
        self.pub.add_to_till(10)
        self.assertEqual(10, self.pub.till)

    def test_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("Beer")
        self.assertEqual("Beer", drink.name)

    def test_find_food_by_name(self):
        food = self.pub.find_food_by_name("Chips")
        self.assertEqual("Chips", food.name)

    def test_carding_customer__legal(self):
        can_buy = self.pub.card_customer(self.customer1)
        self.assertEqual(True, can_buy)

    def test_carding_customer__minor(self):
        cannot_buy = self.pub.card_customer(self.customer2)
        self.assertEqual(False, cannot_buy)

    def test_get_customer_state(self):
        self.customer1.drink_the_drink(self.drink2)
        self.customer1.drink_the_drink(self.drink2)
        drunkeness_level = self.pub.get_customer_state(self.customer1)
        self.assertEqual(6, drunkeness_level)

    def test_cut_off(self):
        self.customer1.drink_the_drink(self.drink2)
        self.customer1.drink_the_drink(self.drink2)
        self.assertEqual(True, self.pub.cut_off(self.customer1))

    def test_sell_a_drink__success(self):
        self.pub.sell_a_drink(self.customer1, "Beer")
        self.assertEqual(4, self.pub.till)
        self.assertEqual(2, self.customer1.wallet)

    def test_sell_a_drink__not_enough_cash(self):
        self.pub.sell_a_drink(self.customer1, "Whiskey Sour")
        self.assertEqual(0, self.pub.till)
        self.assertEqual(6, self.customer1.wallet)

    def test_sell_a_drink__not_found(self):
        self.pub.sell_a_drink(self.customer1, "Pina Collada")
        self.assertEqual(0, self.pub.till)
        self.assertEqual(6, self.customer1.wallet)

    def test_sell_a_drink__minor(self):
        self.pub.sell_a_drink(self.customer2, "Beer")
        self.assertEqual(0, self.pub.till)
        self.assertEqual(6, self.customer1.wallet)

    def test_sell_a_drink__too_drunk(self):
        self.pub.sell_a_drink(self.customer3, "Beer")
        self.pub.sell_a_drink(self.customer3, "Beer")
        self.assertEqual(8, self.pub.till)
        self.assertEqual(42, self.customer3.wallet)

    def test_sell_food(self):
        self.pub.sell_a_drink(self.customer3, "Beer")
        self.pub.sell_food(self.customer3, "Chips")
        self.assertEqual(43, self.customer3.wallet)
        self.assertEqual(1, self.pub.get_customer_state(self.customer3))

    def test_drink_names(self):
        drink_list = self.pub.drink_names(self.pub.drinks)
        self.assertEqual(['Whiskey Sour', 'Beer', 'Wine'], drink_list)

    def test_drinks_customer_can_afford(self):
        customer = self.customer1
        drinks_menu = self.pub.drinks
        affordable_drinks = self.pub.drinks_customer_can_afford(customer, drinks_menu)
        self.assertEqual(["Beer", "Wine"], affordable_drinks)
