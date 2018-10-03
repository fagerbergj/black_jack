import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
import pytest

from deck import Deck
from card import Card
from hand import Hand
from player import Player


class TestPlayer(object):

    @classmethod
    def setup_class(cls):
        cls.player = Player("Jason", 100)

    def test_player(self):
        assert self.player.name == "Jason"
        assert self.player.money == 100

    @mock.patch("player.print")
    def test_status(self, m):
        hand = Hand([Card("Jack", "Hearts")])
        self.player.hand = hand
        self.player.status()
        m.assert_called_once_with("Player's Remaining Money: {}\n Player Hand: {}".format(self.player.money, self.player.curr_hand))

    @mock.patch("player.print")
    def test_bet(self, m):
        hand = Hand([Card("Jack", "Hearts")])
        self.player.hand = hand
        self.player.bet(40)
        assert self.player.money == 60 and self.player.curr_bet == 40

    @mock.patch('player.input')
    def test_valid_bet(self, mock_input):
        mock_input.side_effect = ["40"]
        assert self.player.get_valid_bet(20) == 40 

    @mock.patch('player.input')
    def test_invalid_high_bet(self, mock_input):
        mock_input.side_effect = ["21446", "21450", "123456789", "50"]
        assert self.player.get_valid_bet(50) == 50

    @mock.patch('player.input')
    def test_invalid_low_bet(self, mock_input):
        mock_input.side_effect = ["9", "1", "0", "10"]
        assert self.player.get_valid_bet(10) == 10