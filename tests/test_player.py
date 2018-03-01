from black_jack.deck import Deck
from black_jack.card import Card
from black_jack.player import Player

class TestPlayer():
    def test_player(self):
        hand = [Card(11,"Hearts")]
        test = Player("Jason", 100, hand)
        assert test.hand == hand
        assert test.name == "Jason"
        assert test.money == 100