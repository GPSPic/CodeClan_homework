class Room:
    def __init__(self, number_id, room_type, capacity, song_list, price):
        self.number_id = number_id
        self.room_type = room_type
        self.capacity = capacity
        self.song_list = song_list
        self.price = price
        self.drink_list = []
        self.tab = 0
        self.guest_list = []

    def get_occupancy(self):
        return len(self.guest_list)
    
    def can_check_in(self, guest):
        if guest in self.guest_list:
            return False
        if self.get_occupancy() >= self.capacity:
            return False
        if not guest.can_pay_for_item(self.price):
            return False
        else:
            return True

    def check_in(self, guest):
        if self.can_check_in(guest):
            self.guest_list.append(guest)
            guest.reduce_wallet(self.price)
            self.tab += self.price

    def check_out(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def cheer_for_fav_song(self, guest):
        if guest.favourite_song in self.song_list:
            print ("Yaas")
            return "Yaas"
        
    def group_can_afford_item(self, item):
        guests_pooled_money = 0
        for guest in self.guest_list:
            guests_pooled_money += guest.get_wallet()
        return guests_pooled_money >= item.price
    
    def charge_group_and_add_song(self, song):
        song_remaining_balance = song.price
        if self.group_can_afford_item(song):
            self.add_song(song)
            for guest in self.guest_list:
                while guest.get_wallet() >= 1 and song_remaining_balance > 0:
                    guest.reduce_wallet(1)
                    song_remaining_balance -= 1

