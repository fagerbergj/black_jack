import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
import pytest

from dealer import Dealer
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
        
    def test_valid_bet(self, mock_input):
        mock_input.side_effect = ["40"]
        assert self.game.get_valid_bet() == 40 

    def test_invalid_high_bet(self, mock_input):
        mock_input.side_effect = ["21446","21450","123456789", "50"]
        assert self.game.get_valid_bet() == 50

    def test_invalid_low_bet(self, mock_input):
        mock_input.side_effect = ["9","1","0", "10"]
        assert self.game.get_valid_bet() == 10

    @pytest.mark.parametrize("move", [
        "h", "s"
    ])
    def test_valid_move_hit_stay(self, mock_input, move):
        assert self.game.is_valid_move(move)

    def test_valid_move_split(self, mock_input):
        h = [Card("Ace", "Clubs"), Card("Ace", "Clubs")]
        self.game.player.curr_hand = h
        self.game.player.money = 20
        self.game.player.curr_bet = 10
        assert self.game.is_valid_move("sp")

    def test_invalid_move_split_different_card_values(self, mock_input):
        h = [Card("Ace", "Clubs"), Card(4, "Clubs")]
        self.game.player.curr_hand = h
        self.game.player.money = 20
        self.game.player.curr_bet = 10
        assert not self.game.is_valid_move("sp")

    def test_invalid_move_split_not_enough_money(self, mock_input):
        h = [Card("Ace", "Clubs"), Card("Ace", "Clubs")]
        self.game.player.curr_hand = h
        self.game.player.money = 10
        self.game.player.curr_bet = 15
        assert not self.game.is_valid_move("sp")

    def test_invalid_move(self, mock_input):
        assert not self.game.is_valid_move("x") and not self.game.is_valid_move("shgs")

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

    def test_double_insufficent_money_is_invalid_move(self, mock_input):
        self.game.player.curr_bet = 9999
        self.game.player.money = 0
        assert not self.game.is_valid_move("d")

    def test_double_sufficent_money_is_valid_move(self, mock_input):
        self.game.player.curr_bet = 1
        self.game.player.money = 3
        assert self.game.is_valid_move("d")

    def test_double_doubles_bet_subtracts_money_and_hits(self, mock_input):
        inital_amount_of_cards = len(self.game.player.curr_hand)
        self.game.player.curr_bet = 20
        self.game.player.money = 30
        self.game.double()
        assert self.game.player.curr_bet == 40
        assert self.game.player.money == 10
        assert len(self.game.player.curr_hand) == inital_amount_of_cards + 1

    
