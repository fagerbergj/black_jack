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


class TestGame(object):

    def setup_method(self):
        self.input_patcher = mock.patch("game.input", side_effect=["1100", "10", "Tom", "21445"])
        self.mock_input = self.input_patcher.start()
        self.game = Game()

    def teardown_method(self):
        self.input_patcher.stop()

    def test_game(self):
        assert self.game.dealer.house_money == 1100
        assert self.game.player.name == "Tom" and self.game.player.money == 21445
        assert self.game.turn_manager.popleft() is self.game.player
        assert self.game.turn_manager.popleft() is self.game.dealer
        assert self.game.min == 10

    @mock.patch("game.Game.hit")
    def test_player_move_hit(self, mock_hit):
        self.game.player_move("h")
        mock_hit.assert_called_once_with()

    @mock.patch("game.Game.stay")
    def test_player_move_stay(self, mock_stay):
        self.game.player_move("s")
        mock_stay.assert_called_once()

    @mock.patch("game.Game.double")
    def test_player_move_stay(self, mock_double):
        self.game.player_move("d")
        mock_double.assert_called_once()

    def test_hit_adds_card(self):
        hand_len_before = len(self.game.player.curr_hand)
        self.game.hit()
        assert len(self.game.player.curr_hand) == hand_len_before + 1

    def test_stay_doesnt_add_card(self):
        hand_len_before = len(self.game.player.curr_hand)
        self.game.stay()
        assert len(self.game.player.curr_hand) == hand_len_before   

    def test_double_doubles_bet_subtracts_money_and_hits(self):
        inital_amount_of_cards = len(self.game.player.curr_hand)
        self.game.player.curr_bet = 20
        self.game.player.money = 30
        self.game.double()
        assert self.game.player.curr_bet == 40
        assert self.game.player.money == 10
        assert len(self.game.player.curr_hand) == inital_amount_of_cards + 1

    @mock.patch('game.Game.player_move')
    def test_do_player_input_valid(self, mock_player_move):
        self.game.cur_player = mock_player = mock.Mock()
        moves = ["h", "s"]
        self.mock_input.side_effect = moves
        self.game.do_player_input()
        mock_player_move.assert_has_calls([mock.call(moves[0]), mock.call(moves[1])])
        assert mock_player.status.call_count == 2
        assert mock_player.curr_hand.sum.call_count == 2
        


