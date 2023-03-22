from drink import Drink
from pub import Pub
from food import Food
from customer import Customer

drink1 = Drink("Whiskey Sour", 8.0, 2)
drink2 = Drink("Beer", 4.0, 3)
drink3 = Drink("Wine", 6.0, 1)
drinks_menu = [drink1, drink2, drink3]

print(drinks_menu)

def drink_names(drinks):
    drink_list = []
    for drink in drinks:
        drink_list.append(drink.name)
    print(drink_list)
    return drink_list

drink_names(drinks_menu)