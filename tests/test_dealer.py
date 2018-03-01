from black_jack.deck import Deck
from black_jack.card import Card
from black_jack.player import Player
from black_jack.dealer import Dealer

class TestDealer():

    def setup_method(self, method):
        self.deck = Deck([Card(11,"Hearts"), Card(12,"Spades"), Card(13, "Diamonds"), Card(1, "Clubs"), Card(6, "Hearts")])
        self.hand = [Card(7,"Clubs")]
        self.test = Dealer("Jason", 10000, self.deck, self.hand)

    def test_dealer(self):
        assert self.test.deck == self.deck
        assert self.test.hand == self.hand
        assert self.test.name == "Jason"
        assert self.test.house_money == 10000
    
    def test_draw(self):
        self.test.draw(self.test)
        self.play = Player("Jason", 100, [])
        self.test.draw(self.play)

        expected = [Card(7,"Clubs"), Card(11,"Hearts")]
        for i in range(len(self.test.hand)):
            assert len(self.test.hand) == len(expected) and self.test.hand[i].same_as(expected[i]) 

        expected = [Card(12,"Spades")]
        for i in range(len(self.play.hand)):
            assert len(self.play.hand) == len(expected) and self.play.hand[i].same_as(expected[i])