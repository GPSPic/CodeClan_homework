class Room:
    def __init__(self, number_id, room_type, capacity, song_list, entry_fee):
        self.number_id = number_id
        self.room_type = room_type
        self.capacity = capacity
        self.song_list = song_list
        self.entry_fee = entry_fee
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
        if not guest.can_pay_for_item(self.entry_fee):
            return False
        else:
            return True

    def check_in(self, guest):
        if self.can_check_in(guest):
            self.guest_list.append(guest)
            guest.reduce_wallet(self.entry_fee)
            self.tab += self.entry_fee

    def check_out(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def cheer_for_fav_song(self, guest):
        if guest.favourite_song in self.song_list:
            print ("Yaas")
            return "Yaas"