import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
from deck import Deck
from card import Card
from player import Player
from dealer import Dealer

class TestDealer():

    def setup_method(self, method):
        self.deck = Deck([Card(11,"Hearts"), Card(12,"Spades"), Card(13, "Diamonds"), Card(1, "Clubs"), Card(6, "Hearts")])
        self.hand = [Card(7,"Clubs")]
        self.test = Dealer("Jason", 10000, self.hand, self.deck)

    def test_dealer(self):
        assert self.test.deck == self.deck
        assert self.test.hand == self.hand
        assert self.test.name == "Jason"
        assert self.test.house_money == 10000
    
    def test_draw(self):
        self.test.draw()
        self.play = Player("Jason", 100, [])
        self.test.draw(self.play)
        

        expected = [Card(7,"Clubs"), Card(11,"Hearts")]
        for i in range(len(self.test.hand)):
            assert len(self.test.hand) == len(expected) and self.test.hand[i].same_as(expected[i]) 

        expected = [Card(12,"Spades")]
        for i in range(len(self.play.hand)):
            assert len(self.play.hand) == len(expected) and self.play.hand[i].same_as(expected[i])

    def test_draw_empty(self):
        empty = Dealer("E", 300, [], Deck([]))
        empty.draw()
        assert empty.deck.size() = 52 * 4 - 1

    @mock.patch("dealer.print")
    def test_status(self, m):
        self.test.status()
        m.assert_called_once_with("Dealer's Remaining Money: {}\n Dealer Hand: {}".format(self.test.house_money, self.test.hand))