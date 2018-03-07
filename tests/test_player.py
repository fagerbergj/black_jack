import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

from deck import Deck
from card import Card
from player import Player

class TestPlayer():
    def test_player(self):
        hand = [Card(11,"Hearts")]
        test = Player("Jason", 100, hand)
        assert test.hand == hand
        assert test.name == "Jason"
        assert test.money == 100