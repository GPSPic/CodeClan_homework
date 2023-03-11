class Venue:
    def __init__(self, rooms):
        self.name = "The Sore Sort"
        self.rooms = rooms
        self.till = 0

    def find_room_by_fanciness(self, fanciness_level):
        matching_rooms = []
        for room in self.rooms:
            if fanciness_level in room.room_type:
                matching_rooms.append(room)
        # [room for room in self.rooms if fanciness_level == room.room_type]
        if matching_rooms == []:
            matching_rooms = "There is no such room"
        return matching_rooms


    def assign_room_to_guest(self, guest, fanciness):
        matching_rooms = self.find_room_by_fanciness(fanciness)
        room_check = len(matching_rooms)
        if matching_rooms == "There is no such room":
            return matching_rooms
        else:
            while room_check > 0:
                for room in matching_rooms:
                    if room.capacity > room.get_occupancy():
                        room.check_in(guest)
                        return "You will find your room this way"
                    else:
                        room_check -= 1
            return "Sorry, all booked!"



    # collect room tabs add to till