import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
from dealer import Dealer
from player import Player
from game import Game

class TestGame():
    @mock.patch("game.input", side_effect=["Bob", "1100", "Tom", "21445"])
    def test_game(self, mock_input):
        game = Game()
        assert game.dealer.name == "Bob" and game.dealer.house_money == 1100
        assert game.player.name == "Tom" and game.player.money == 21445
