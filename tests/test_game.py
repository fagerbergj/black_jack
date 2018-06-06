import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
from dealer import Dealer
from player import Player
from game import Game
from card import Card

@mock.patch("game.input")
class TestGame():

    def setup_method(self):
        with mock.patch("game.input", side_effect=["1100", "10", "Tom", "21445"]):
            self.game = Game()

    def test_game(self, mock_input):
        assert self.game.dealer.house_money == 1100
        assert self.game.player.name == "Tom" and self.game.player.money == 21445

    def test_sum_hand_no_ace(self, mock_input):
        h = [Card(10, "Hearts"), Card(2, "Clubs")]
        assert self.game.sum_hand(h) == {12}

    def test_sum_hand_has_ace(self, mock_input):
        h = [Card(8, "Hearts"), Card("Ace", "Clubs")]
        assert self.game.sum_hand(h) == {19,9}

    def test_sum_hand_has_multi_ace(self, mock_input):
        h = [Card(8, "Hearts"), Card("Ace", "Clubs"), Card("Ace", "Clubs")]
        assert self.game.sum_hand(h) == {10,20}

    def test_sum_hand_worst_case(self, mock_input):
        h = [Card("Ace", "Clubs")] * 16
        assert self.game.sum_hand(h) == {16}

    def test_sum_hand_equals_21(self, mock_input):
        h = [Card("Ace", "Clubs"), Card(10, "Clubs")]
        assert self.game.sum_hand(h) == {11, 21}

    def test_set_min(self, mock_input):
        assert self.game.min == 10
        
    def test_valid_bet(self, mock_input):
        mock_input.side_effect = ["40"]
        assert self.game.get_valid_bet(self.game.player.name) == 40 

    def test_invalid_high_bet(self, mock_input):
        mock_input.side_effect = ["21446","21450","123456789", "50"]
        assert self.game.get_valid_bet(self.game.player.name) == 50

    def test_invalid_low_bet(self, mock_input):
        mock_input.side_effect = ["9","1","0", "10"]
        assert self.game.get_valid_bet(self.game.player.name) == 10

    def test_valid_move(self, mock_input):
        assert self.game.is_valid_move("h") and self.game.is_valid_move("s")

    def test_invalid_move(self, mock_input):
        assert not self.game.is_valid_move("x") and not self.game.is_valid_move("shgs")