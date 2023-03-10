class Guest:
    def __init__(self, identifier, wallet, favourite_song):
        self.identifier = identifier
        self.wallet = wallet
        self.favourite_song = favourite_song

    def can_pay_for_item(self, price):
        return self.wallet >= price
    
    def reduce_wallet(self, price):
        if self.can_pay_for_item(price):
            self.wallet -= price

    