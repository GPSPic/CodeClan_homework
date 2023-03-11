import unittest
from classes.song import Song
from classes.drink import Drink
from classes.guest import Guest
from classes.room import Room
from classes.venue import Venue

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("I ran", 5.0)
        self.song2 = Song("Song 2", 4.0)
        self.song3 = Song("Let it go", 30.0)
        self.song4 = Song("More than a feeling", 3.0)
        self.bargain_song_list = [self.song1, self.song2]
        self.standard_song_list = [self.song1, self.song2, self.song3]
        self.luxury_song_list = [self.song1, self.song2, self.song3, self.song4]
        self.guest1 = Guest("John", 50, self.song1)
        self.guest2 = Guest("Paul", 30, self.song2)
        self.guest3 = Guest("George", 20, self.song3)
        self.guest4 = Guest("Ringo", 10, self.song4)
        self.guest5 = Guest("Yoko", 200, self.song1)
        self.drink1 = Drink("Beer", 3)
        self.drink2 = Drink("Gin", 5)
        self.drink3 = Drink("Wine", 4)
        self.drink_list = [self.drink1, self.drink2, self.drink3]
        self.room1 = Room(1, "Bargain", 1, self.bargain_song_list, 10)
        self.room2 = Room(2, "Bargain", 1, self.bargain_song_list, 10)
        self.room3 = Room(3, "Standard", 2, self.standard_song_list, 12)
        self.room4 = Room(4, "Standard", 2, self.standard_song_list, 12)
        self.room5 = Room(5, "Luxury", 3, self.luxury_song_list, 15)
        self.rooms = [self.room1, self.room2, self.room3, self.room4, self.room5]
        self.venue = Venue(self.rooms)

# test 32 - testing class
    def test_venue_has_rooms(self):
        self.assertEqual(5, len(self.rooms))

# test 33 - finding room by room_type (fanciness) - Bargain
    def test_find_room_by_fanciness__bargain(self):
        matching_rooms = self.venue.find_room_by_fanciness("Bargain")
        self.assertEqual([self.room1, self.room2], matching_rooms)

# test 34 - finding room by room_type (fanciness) - Luxury
    def test_find_room_by_fanciness__luxury(self):
        matching_rooms = self.venue.find_room_by_fanciness("Luxury")
        self.assertEqual([self.room5], matching_rooms) 

# test 35 - finding room by room_type (fanciness) - type not found
    def test_find_room_by_fanciness__fanciness_not_found(self):
        matching_rooms = self.venue.find_room_by_fanciness("Deluxe")
        self.assertEqual("There is no such room", matching_rooms) 

# test 36 - assigning room to guest by fanciness request
    def test_assign_room_to_guest_by_fanciness__all_rooms_empty_bargain(self):
        message_to_guest = self.venue.assign_room_to_guest(self.guest1, "Bargain")
        self.assertEqual(1, self.room1.get_occupancy())

# test 37 - assigning room to guest with first requested room full
    def test_assign_room_to_guest_by_fanciness__first_room_full_bargain(self):
        self.venue.assign_room_to_guest(self.guest2, "Bargain")
        self.venue.assign_room_to_guest(self.guest1, "Bargain")
        self.assertEqual(1, self.room1.get_occupancy())
        self.assertEqual(1, self.room2.get_occupancy())

# test 38 - assigning room to guest with all requested bargain rooms full
    def test_assign_room_to_guest_by_fanciness__all_rooms_full_bargain(self):
        this_way2 = self.venue.assign_room_to_guest(self.guest2, "Bargain")
        this_way1 = self.venue.assign_room_to_guest(self.guest1, "Bargain")
        all_booked = self.venue.assign_room_to_guest(self.guest3, "Bargain")
        self.assertEqual(1, self.room1.get_occupancy())
        self.assertEqual(1, self.room2.get_occupancy())
        self.assertEqual("Sorry, all booked!", all_booked)
        self.assertEqual("You will find your room this way", this_way1)
        self.assertEqual("You will find your room this way", this_way2)

# test 39 - assigning room to guest with luxury room full
    def test_assign_room_to_guest_by_fanciness__room_full_luxury(self):
        self.venue.assign_room_to_guest(self.guest2, "Luxury")
        self.venue.assign_room_to_guest(self.guest1, "Luxury")
        self.venue.assign_room_to_guest(self.guest5, "Luxury")
        all_booked = self.venue.assign_room_to_guest(self.guest3, "Luxury")
        self.assertEqual(3, self.room5.get_occupancy())
        self.assertEqual("Sorry, all booked!", all_booked)

# test 40 - cannot assign room as fanciness not matching searched
    def test_assign_room_to_guest_by_fanciness__no_room_type_found(self):
        message_to_guest = self.venue.assign_room_to_guest(self.guest1, "Deluxe")
        self.assertEqual(0, self.room1.get_occupancy())
        self.assertEqual("There is no such room", message_to_guest)