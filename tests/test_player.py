import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
from deck import Deck
from card import Card
from hand import Hand
from player import Player

class TestPlayer():
    def test_player(self):
        hand = Hand([Card("Jack","Hearts")])
        test = Player("Jason", 100, hand)
        assert test.curr_hand == hand
        assert test.name == "Jason"
        assert test.money == 100

    @mock.patch("player.print")
    def test_status(self, m):
        hand = Hand([Card("Jack","Hearts")])
        test = Player("Jason", 100, hand)
        test.status()
        m.assert_called_once_with("Player's Remaining Money: {}\n Player Hand: {}".format(test.money, test.curr_hand))

    @mock.patch("player.print")
    def test_bet(self, m):
        hand = Hand([Card("Jack","Hearts")])
        test = Player("Jason", 100, hand)
        test.bet(40)
        assert test.money == 60 and test.curr_bet == 40