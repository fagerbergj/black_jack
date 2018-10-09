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

    @pytest.mark.parametrize("move", [
        "h", "s"
    ])
    def test_valid_move_hit_stay(self, move):
        assert self.player.is_valid_move(move)

    def test_valid_move_split(self):
        h = Hand([Card("Ace", "Clubs"), Card("Ace", "Clubs")])
        self.player.curr_hand = h
        self.player.money = 20
        self.player.curr_bet = 10
        assert self.player.is_valid_move("sp")

    def test_invalid_move_split_different_card_values(self):
        h = Hand([Card("Ace", "Clubs"), Card(4, "Clubs")])
        self.player.curr_hand = h
        self.player.money = 20
        self.player.curr_bet = 10
        assert not self.player.is_valid_move("sp")

    def test_invalid_move_split_not_enough_money(self):
        h = Hand([Card("Ace", "Clubs"), Card("Ace", "Clubs")])
        self.player.curr_hand = h
        self.player.money = 10
        self.player.curr_bet = 15
        assert not self.player.is_valid_move("sp")

    @pytest.mark.parametrize("move", [
        "x", "shgs"
    ])
    def test_invalid_move(self, move):
        assert not self.player.is_valid_move(move)

    def test_double_insufficent_money_is_invalid_move(self):
        self.player.curr_bet = 9999
        self.player.money = 0
        assert not self.player.is_valid_move("d")

    def test_double_sufficent_money_is_valid_move(self):
        self.player.curr_bet = 1
        self.player.money = 3
        assert self.player.is_valid_move("d")
