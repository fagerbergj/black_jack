import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
from dealer import Dealer
from player import Player
from game import Game
from card import Card

@mock.patch("game.input", side_effect=["Bob", "1100", "Tom", "21445", "10"])
class TestGame():

    def test_game(self, mock_input):
        game = Game()
        assert game.dealer.name == "Bob" and game.dealer.house_money == 1100
        assert game.player.name == "Tom" and game.player.money == 21445

    def test_sum_hand_no_ace(self, mock_input):
        game = Game()
        h = [Card(10, "Hearts"), Card(2, "Clubs")]
        assert game.sum_hand(h) == {12}

    def test_sum_hand_has_ace(self, mock_input):
        game = Game()
        h = [Card(8, "Hearts"), Card("Ace", "Clubs")]
        assert game.sum_hand(h) == {19,9}

    def test_sum_hand_has_multi_ace(self, mock_input):
        game = Game()
        h = [Card(8, "Hearts"), Card("Ace", "Clubs"), Card("Ace", "Clubs")]
        assert game.sum_hand(h) == {10,20}

    def test_sum_hand_worst_case(self, mock_input):
        game = Game()
        h = [Card("Ace", "Clubs")] * 16
        assert game.sum_hand(h) == {16}

    def test_sum_hand_equals_21(self, mock_input):
        game = Game()
        h = [Card("Ace", "Clubs"), Card(10, "Clubs")]
        assert game.sum_hand(h) == {11, 21}

    def test_set_min(self, mock_input):
        game = Game()
        assert game.min == 10
        
    def test_valid_bet(self, mock_input):
        mock_input.side_effect = list(mock_input.side_effect) + ["40"]
        game = Game()
        assert game.get_valid_bet() == 40

    def test_invalid_high_bet(self, mock_input):
        mock_input.side_effect = list(mock_input.side_effect) + ["21446","21450","123456789", "50"]
        game = Game()
        assert game.get_valid_bet() == 50

    def test_invalid_low_bet(self, mock_input):
        mock_input.side_effect = list(mock_input.side_effect) + ["9","1","0", "10"]
        game = Game()
        assert game.get_valid_bet() == 10