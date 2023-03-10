import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("I ran", 5.0)

    def test_song_has_name(self):
        self.assertEqual("I ran", self.song.name)

    def test_song_has_price(self):
        self.assertEqual(5, self.song.licensing_fee)