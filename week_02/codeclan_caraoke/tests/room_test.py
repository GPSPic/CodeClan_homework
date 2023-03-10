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
        self.room1 = Room(1, "Bargain", 1, self.bargain_song_list, 5)
        self.room2 = Room(2, "Bargain", 1, self.bargain_song_list, 5)
        self.room3 = Room(3, "Standard", 2, self.standard_song_list, 7)
        self.room4 = Room(4, "Standard", 2, self.standard_song_list, 7)
        self.room5 = Room(4, "Luxury", 3, self.luxury_song_list, 10)

        