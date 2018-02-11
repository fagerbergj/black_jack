from deck import Deck
from card import Card

class TestDeck():
    def test_deck(self):
        cards = [Card(11,"Hearts"), Card(12,"Spades"), Card(13, "Diamonds"), Card(1, "Clubs"), Card(6, "Hearts")]
        test = Deck(cards)
        while len(test.cards) > 0:
            x = test.draw()
            assert x in cards
    
    def test_draw(self):
        cards = [Card(11,"Hearts"), Card(12,"Spades"), Card(13, "Diamonds"), Card(1, "Clubs"), Card(6, "Hearts")]
        test = Deck(cards)
        card = test.draw()
        assert card in cards and len(test.cards) == len(cards) - 1

    def test_shuffle(self):
        cards = [Card(11,"Hearts"), Card(12,"Spades"), Card(13, "Diamonds"), Card(1, "Clubs"), Card(6, "Hearts")]
        test = Deck(cards)
        test.shuffle
        assert cards == test.cards