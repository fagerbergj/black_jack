from deck import Deck
from card import Card

class TestDeck():
    def test_deck(self):
        cards = [Card(11,"Hearts"), Card(12,"Spades"), Card(13, "Diamonds"), Card(1, "Clubs"), Card(6, "Hearts")]
        test = Deck(cards)
        while not test.cards.empty():
            x = test.cards.get()
            assert x in cards
    
    def test_draw(self):
        cards = [Card(11,"Hearts"), Card(12,"Spades"), Card(13, "Diamonds"), Card(1, "Clubs"), Card(6, "Hearts")]
        test = Deck(cards)
        card = test.draw()
        assert card in cards and test.cards.qsize() == len(cards) - 1