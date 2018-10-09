import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
import pytest

from dealer import Dealer
from hand import Hand
from player import Player
from game import Game
from card import Card

@mock.patch("game.input")
class TestGame(object):

    def setup_method(self):
        with mock.patch("game.input", side_effect=["1100", "10", "Tom", "21445"]):
            self.game = Game()

    def test_game(self, mock_input):
        assert self.game.dealer.house_money == 1100
        assert self.game.player.name == "Tom" and self.game.player.money == 21445
        assert self.game.turn_manager.popleft() is self.game.player
        assert self.game.turn_manager.popleft() is self.game.dealer

    def test_set_min(self, mock_input):
        assert self.game.min == 10

    @mock.patch("game.Game.hit")
    def test_player_move_hit(self, mock_hit, mock_input):
        self.game.player_move("h")
        mock_hit.assert_called_once_with()

    @mock.patch("game.Game.stay")
    def test_player_move_stay(self, mock_stay, mock_input):
        self.game.player_move("s")
        mock_stay.assert_called_once()

    def test_hit_adds_card(self, mock_input):
        hand_len_before = len(self.game.player.curr_hand)
        self.game.hit()
        assert len(self.game.player.curr_hand) == hand_len_before + 1

    def test_stay_doesnt_add_card(self, mock_input):
        hand_len_before = len(self.game.player.curr_hand)
        self.game.stay()
        assert len(self.game.player.curr_hand) == hand_len_before   

    def test_double_doubles_bet_subtracts_money_and_hits(self, mock_input):
        inital_amount_of_cards = len(self.game.player.curr_hand)
        self.game.player.curr_bet = 20
        self.game.player.money = 30
        self.game.double()
        assert self.game.player.curr_bet == 40
        assert self.game.player.money == 10
        assert len(self.game.player.curr_hand) == inital_amount_of_cards + 1

    
