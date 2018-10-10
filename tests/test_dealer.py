import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import mock
import pytest
from deck import Deck
from card import Card
from hand import Hand, HandBustException
from player import Player
from dealer import Dealer

class TestDealer(object):

    def same_card(self, c1, c2):
        return c1.name == c2.name and c1.suit == c2.suit

    def setup_method(self, method):
        self.deck = Deck([Card("Jack","Hearts"), Card("Queen","Spades"), Card("King", "Diamonds"), Card("Ace", "Clubs"), Card(6, "Hearts")])
        self.hand = Hand([Card(7,"Clubs")])
        self.test = Dealer( 10000, self.hand, self.deck)

    def test_dealer(self):
        assert self.test.deck == self.deck
        assert self.test.hand == self.hand
        assert self.test.house_money == 10000
    
    def test_draw(self):
        self.test.draw()

        expected = Hand([Card(7,"Clubs"), Card("Jack","Hearts")])
        for i in range(len(self.test.hand)):
            assert len(self.test.hand) == len(expected) and self.same_card(self.test.hand[i], expected[i]) 

        self.play = Player("Jason", 100, [])
        self.test.draw(self.play)

        expected = Hand([Card("Queen","Spades")])
        for i in range(len(self.play.curr_hand)):
            assert len(self.play.curr_hand) == len(expected)  and self.same_card(self.play.curr_hand[i], expected[i]) 

    def test_draw_empty(self):
        empty = Dealer(300, Hand(), Deck([]))
        empty.draw()
        assert empty.deck.size() == 52 * 4 - 1

    @mock.patch("dealer.print")
    def test_status(self, m):
        self.test.status()
        m.assert_called_once_with("Dealer's Remaining Money: {}\n Dealer Hand: {}".format(self.test.house_money, self.test.hand))

    def test_move_draws_until_sum_equal_17(self):
        original_hand_count = len(self.test.hand)        
        self.test.move()
        assert len(self.test.hand) == original_hand_count + 1
        assert max(self.hand.sum()) == 17

    def test_move_draws_until_sum_gte_17_but_lt_22(self):
        self.test.deck = Deck([Card(7, "Clubs"), Card(4, "Clubs")])
        original_hand_count = len(self.test.hand)        
        self.test.move()
        assert len(self.test.hand) == original_hand_count + 2
        hand_sum = max(self.hand.sum())
        assert hand_sum >= 17 and hand_sum < 22

    def test_move_draws_until_bust(self):
        self.test.deck = Deck([Card(9, "Clubs"), Card(10, "Clubs")])
        original_hand_count = len(self.test.hand)        
        self.test.move()
        assert len(self.test.hand) == original_hand_count + 2
        with pytest.raises(HandBustException):
            self.test.hand.sum()