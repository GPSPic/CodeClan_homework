import unittest
from classes.song import Song
from classes.drink import Drink
from classes.guest import Guest
from classes.room import Room

class TestRoom(unittest.TestCase):
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
        self.drink1 = Drink("Beer", 3)
        self.drink2 = Drink("Gin", 5)
        self.drink3 = Drink("Wine", 4)
        self.drink_list = [self.drink1, self.drink2, self.drink3]
        self.room1 = Room(1, "Bargain", 1, self.bargain_song_list, 10)
        self.room2 = Room(2, "Bargain", 1, self.bargain_song_list, 10)
        self.room3 = Room(3, "Standard", 2, self.standard_song_list, 12)
        self.room4 = Room(4, "Standard", 2, self.standard_song_list, 12)
        self.room5 = Room(4, "Luxury", 3, self.luxury_song_list, 15)

# test 11 - tests entry fee and interaction with Guest
    def test_guest_can_pay_for_room__true(self):
        fee = self.room1.price
        self.assertTrue(self.guest4.can_pay_for_item(fee))
    
#  test 12 - failure condition for test 11
    def test_guest_can_pay_for_room__not_enough_money(self):
        fee = self.room3.price
        self.assertFalse(self.guest4.can_pay_for_item(fee))

# test 13 - used for check_in and potential reassignment to another room later
    def test_get_occupancy__empty(self):
        self.assertEqual(0, self.room1.get_occupancy())

#  test 14 - second test for occupancy
    def test_get_occupancy__one_guest(self):
        self.room1.guest_list = [self.guest1]
        self.assertEqual(1, self.room1.get_occupancy())

# test 15 - setting condition allowing guest to check_in (money, capacity)
    def test_can_check_in__true(self):
        self.assertTrue(self.room1.can_check_in(self.guest1))

#  test 16 - test 15 fail condition for lack of money
    def test_can_check_in__not_enough_money(self):
        self.assertFalse(self.room5.can_check_in(self.guest4))

#  test 17 - test 15 fail condition for lack of room capacity
    def test_can_check_in__room_full(self):
        self.room1.guest_list = [self.guest2]
        self.assertFalse(self.room1.can_check_in(self.guest1))

# test 18 - test 15 fail condition for guest already checked in
    def test_can_check_in__already_checked_in(self):
        self.room3.guest_list = [self.guest1]
        self.assertFalse(self.room3.can_check_in(self.guest1))

# test 19 - result of guest check_in
    def test_check_guest_in(self):
        self.room3.check_in(self.guest1)
        self.room3.check_in(self.guest2)
        self.assertEqual(2, self.room3.get_occupancy())
        self.assertEqual(38, self.guest1.get_wallet())
        self.assertEqual(18, self.guest2.get_wallet())

#  test 20 - test check_out success
    def test_check_out__success(self):
        self.room3.check_in(self.guest1)
        self.room3.check_in(self.guest2)
        self.room3.check_out(self.guest1)
        self.assertEqual(1, self.room3.get_occupancy())

#  test 21 - test if check out guest if not in guest_list
    def test_check_out__no_guest_found(self):
        self.room3.check_in(self.guest1)
        self.room3.check_out(self.guest2)
        self.assertEqual(1, self.room3.get_occupancy())

# test 22 - add a song to a room playlist
    def test_add_song_to_playlist(self):
        self.room1.add_song(self.song3)
        self.assertEqual(3, len(self.room1.song_list))


#  test 23 - guest cheers if their fav song is in the room
    def test_guest_cheers_for_fav_song(self):
        self.room2.check_in(self.guest2)
        cheer = self.room2.cheer_for_fav_song(self.guest2)
        self.assertEqual("Yaas", cheer)

# test 24 - no cheer if fav song not in list
    def test_guest_cheers_for_fav_song__false(self):
        self.room2.check_in(self.guest4)
        cheer = self.room2.cheer_for_fav_song(self.guest4)
        self.assertIsNone(cheer)

#  test 25 - add entry fees to a daily tab for the room by updating check_in()
    def test_add_price_to_room_tab(self):
        self.room5.check_in(self.guest2)
        self.room5.check_in(self.guest3)
        self.assertEqual(30, self.room5.tab)

# test 27 - one or more guests can afford to add a song to a playlist
    def test_can_afford_to_add_song_to_room_playlist__true(self):
        self.room3.check_in(self.guest2)
        self.room3.check_in(self.guest3)
        group_can_afford = self.room3.group_can_afford_item(self.song4)
        self.assertTrue(group_can_afford)
        # self.assertEqual(18, self.guest2.get_wallet())
        # self.assertEqual(8, self.guest3.get_wallet())

#  test 28 - test 28 fail condition for not enough pooled money
    def test_can_afford_to_add_song_to_room_playlist__false(self):
        self.room5.check_in(self.guest2)
        self.room5.check_in(self.guest3)
        group_can_afford = self.room3.group_can_afford_item(self.song3)
        self.assertFalse(group_can_afford)


#  test 29 - test to have guest pay to add a song to a room's playlist
    def test_charge_fee_to_group_to_add_song_to_room_list__1_guest(self):
        self.room3.check_in(self.guest2)
        self.room3.charge_group_and_add_song(self.song4)
        self.assertEqual(4, len(self.room3.song_list))
        self.assertEqual(15, self.guest2.get_wallet())

# test 30 - test to have several guests pay to add a song to the room's playlist
    def test_charge_fee_to_group_to_add_song_to_room_list__2_guests(self):
        self.room3.check_in(self.guest2)
        self.room3.check_in(self.guest1)
        self.room3.charge_group_and_add_song(self.song3)
        self.assertEqual(4, len(self.room3.song_list))
        self.assertEqual(0, self.guest2.get_wallet())
        self.assertEqual(26, self.guest1.get_wallet())

# test 31 - guest cannot add song due to lack of funds
    def test_charge_fee_to_group_to_add_song_to_room_list__not_enough_money(self):
        self.room3.check_in(self.guest2)
        self.room3.check_in(self.guest3)
        self.room3.charge_group_and_add_song(self.song3)
        self.assertEqual(3, len(self.room3.song_list))
        self.assertEqual(18, self.guest2.get_wallet())
        self.assertEqual(8, self.guest3.get_wallet())   