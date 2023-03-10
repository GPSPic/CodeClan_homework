class Room:
    def __init__(self, number_id, room_type, capacity, song_list, entry_fee):
        self.number_id = number_id
        self.room_type = room_type
        self.capacity = capacity
        self.song_list = song_list
        self.entry_fee = entry_fee
        self.drink_list = []
        self.tab = 0

