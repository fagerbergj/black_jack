from deck import Deck
from card import Card
from player import Player
from dealer import Dealer

class TestDealer():

    def setup_method(self, method):
        self.deck = Deck([Card(11,"Hearts"), Card(12,"Spades"), Card(13, "Diamonds"), Card(1, "Clubs"), Card(6, "Hearts")])
        self.hand = [Card(7,"7")]
        self.test = Dealer("Jason", 10000, self.deck, self.hand)

    def test_dealer(self):
        assert self.test.deck == self.deck
        assert self.test.hand == self.hand
        assert self.test.name == "Jason"
        assert self.test.house_money == 10000
    
    def test_draw(self):
        self.test.draw(self.test)
        play = Player("Jason", 100, [])
        self.test.draw(play)

        assert self.test.hand == [Card(7,"7"), Card(11,"Hearts")]
        assert self.play.hand == [Card(12,"Spades")]