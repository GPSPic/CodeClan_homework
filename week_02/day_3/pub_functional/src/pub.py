
class Pub:
    def __init__(self, name, till, drinks, food, stock):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.food = food
        self.stock = stock

    # def has_drink(self, drink):
    #     if drink.name in self.drinks:
    #         return True

    def add_to_till(self, amount):
        self.till += amount

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
            # else:
            #     return "Drink does not exist"

    def card_customer(self, customer):
         return customer.age >= 18

    def get_customer_state(self, customer):
         return customer._drunkeness

    def cut_off(self, customer):
         return customer._drunkeness > 5       

    def sell_a_drink(self, customer, drink_name):
        drink = self.find_drink_by_name(drink_name)
        if drink != None and self.card_customer(customer) and customer.can_pay_for_drink_or_food(drink.price):
                customer.reduce_wallet(drink.price)
                self.add_to_till(drink.price)
                customer.drink_the_drink(drink)

    def find_food_by_name(self, food_name):
        for food in self.food:
            if food.name == food_name:
                return food

    def sell_food(self, customer, food_name):
         food = self.find_food_by_name(food_name)
         if food != None and customer.can_pay_for_drink_or_food(food.price):
              customer.reduce_wallet(food.price)
              customer.eat_the_food(food)

    def drink_names(self, drinks):
        drink_list = [drink.name for drink in drinks]
        return drink_list        
        # drink_list = []
        # for drink in drinks:
        #     drink_list.append(drink.name)
        # return drink_list
        
    def drinks_customer_can_afford(self, customer, drink_menu):
        affordable_drinks = [drink.name for drink in drink_menu if customer.can_pay_for_drink_or_food(drink.price)]      
        return affordable_drinks
        # affordable_drinks = []
        # for drink in drink_menu:
        #         if customer.can_pay_for_drink_or_food(drink.price):
        #            affordable_drinks.append(drink.name)
        # return affordable_drinks



#  and self.cut_off == False 

            
    # def get_customer_age(self, customer):
    #     # if customer.age >= 18:
    #     #     return True
    #     # else:
    #     #     return False
    #     return customer.age >= 18

    # def customer_too_drunk(self, customer):
    #     pass