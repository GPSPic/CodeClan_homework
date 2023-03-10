import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("I ran", 5.0)
        self.song2 = Song("Song 2", 4.0)
        self.song3 = Song("Let it go", 30)
        self.song4 = Song("More than a feeling", 3)
        self.guest1 = Guest("John", 50, self.song1)
        self.guest2 = Guest("Paul", 30, self.song2)
        self.guest3 = Guest("George", 20, self.song3)
        self.guest4 = Guest("Ringo", 10, self.song4)


    def test_guest_has_name(self):
        self.assertEqual("John", self.guest1.identifier)

    def test_guest_has_money(self):
        self.assertEqual(10, self.guest4.wallet)

    def test_guest_has_favourite_song(self):
        song = self.guest3.favourite_song.name
        self.assertEqual("Let it go", song)

    def test_guest_can_pay_for_item__true(self):
        can_pay = self.guest1.can_pay_for_item(self.song1.licensing_fee)
        self.assertTrue(can_pay)

    def test_gest_can_pay_for_item__not_enough_money(self):
        song = self.guest4.favourite_song.licensing_fee
        cannot_pay = self.guest4.can_pay_for_item(song)

    def test_guest_reduce_wallet(self):
        price = self.guest3.favourite_song.licensing_fee
        self.guest1.reduce_wallet(price)
        self.assertEqual(20, self.guest1.wallet)

    