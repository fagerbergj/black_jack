import mock
from black_jack.dealer import Dealer
from black_jack.player import Player
from black_jack.game import Game

class TestGame():
    @mock.patch("black_jack.game.input", side_effect=["Bob", 1100, "Tom", 21445])
    def test_game(self, mock_input):
        game = Game()
        assert game.dealer.name == "Bob" and game.dealer.house_money == 1100
        assert game.player.name == "Tom" and game.player.money == 21445
