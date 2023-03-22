class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self._drunkeness = 0

    def can_pay_for_drink_or_food(self, amount):
        return self.wallet >= amount
    
    def reduce_wallet(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount
    
    def drink_the_drink(self, drink):
        self._drunkeness += drink.alcohol_level

    def eat_the_food(self, food):
        self._drunkeness -= food.rejuvenation_level
