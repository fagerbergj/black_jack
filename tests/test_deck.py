import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

from deck import Deck
from card import Card

class TestDeck():
    def test_deck(self):
        cards = [Card("Jack","Hearts"), Card("Queen","Spades"), Card("King", "Diamonds"), Card("Ace", "Clubs"), Card(6, "Hearts")]
        test = Deck(cards)
        while len(test.cards) > 0:
            x = test.draw()
            assert x in cards

    
    def test_draw(self):
        cards = [Card("Jack","Hearts"), Card("Queen","Spades"), Card("King", "Diamonds"), Card("Ace", "Clubs"), Card(6, "Hearts")]
        test = Deck(cards)
        card = test.draw()
        assert card in cards and len(test.cards) == len(cards) - 1

    def test_shuffle(self):
        cards = [Card("Jack","Hearts"), Card("Queen","Spades"), Card("King", "Diamonds"), Card("Ace", "Clubs"), Card(6, "Hearts")]
        test = Deck(cards)
        test.shuffle()
        assert cards == test.cards

    def test_default_deck(self):
        test = Deck()
        assert len(test.cards) == 52 * 4