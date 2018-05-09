import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
from deck import Deck
from card import Card
from player import Player

class TestPlayer():
    def test_player(self):
        hand = [Card("Jack","Hearts")]
        test = Player("Jason", 100, hand)
        assert test.hand == hand
        assert test.name == "Jason"
        assert test.money == 100

    @mock.patch("player.print")
    def test_status(self, m):
        hand = [Card("Jack","Hearts")]
        test = Player("Jason", 100, hand)
        test.status()
        m.assert_called_once_with("Player's Remaining Money: {}\n Player Hand: {}".format(test.money, test.hand))

    @mock.patch("player.input", side_effect=["40"])
    def test_valid_bet(self, m):
        hand = [Card("Jack","Hearts")]
        test = Player("Jason", 100, hand)
        test.bet()
        assert test.money == 60

    @mock.patch("player.input", side_effect=["400", "200", "101", "25"])
    def test_invalid_bet(self, m):
        hand = [Card("Jack","Hearts")]
        test = Player("Jason", 100, hand)
        test.bet()
        assert test.money == 75