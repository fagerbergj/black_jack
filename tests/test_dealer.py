import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
from deck import Deck
from card import Card
from player import Player
from dealer import Dealer

class TestDealer():

    def same_card(self, c1, c2):
        print()
        return c1.name == c2.name and c1.suit == c2.suit

    def setup_method(self, method):
        self.deck = Deck([Card("Jack","Hearts"), Card("Queen","Spades"), Card("King", "Diamonds"), Card("Ace", "Clubs"), Card(6, "Hearts")])
        self.hand = [Card(7,"Clubs")]
        self.test = Dealer("Jason", 10000, self.hand, self.deck)

    def test_dealer(self):
        assert self.test.deck == self.deck
        assert self.test.hand == self.hand
        assert self.test.name == "Jason"
        assert self.test.house_money == 10000
    
    def test_draw(self):
        self.test.draw()

        expected = [Card(7,"Clubs"), Card("Jack","Hearts")]
        for i in range(len(self.test.hand)):
            assert len(self.test.hand) == len(expected) and self.same_card(self.test.hand[i], expected[i]) 

        self.play = Player("Jason", 100, [])
        self.test.draw(self.play)

        expected = [Card("Queen","Spades")]
        for i in range(len(self.play.hand)):
            assert len(self.play.hand) == len(expected)  and self.same_card(self.play.hand[i], expected[i]) 

    def test_draw_empty(self):
        empty = Dealer("E", 300, [], Deck([]))
        empty.draw()
        assert empty.deck.size() == 52 * 4 - 1

    @mock.patch("dealer.print")
    def test_status(self, m):
        self.test.status()
        m.assert_called_once_with("Dealer's Remaining Money: {}\n Dealer Hand: {}".format(self.test.house_money, self.test.hand))