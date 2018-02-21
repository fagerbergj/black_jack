
from random import shuffle
from card import Card

class Deck():
    def __init__(self, cards):
        self.cards = cards
        if(len(cards) == 0):
            self.default_deck()
    
    def draw(self):
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card

    def shuffle(self):
        shuffle(self.cards)

    def default_deck(self):
        self.cards = [Card(2,"Hearts"), Card(2,"Diamonds"), Card(2,"Spades"), Card(2,"Clubs"),
        Card(3,"Hearts"), Card(3,"Diamonds"), Card(3,"Spades"), Card(3,"Clubs"),
        Card(4,"Hearts"), Card(4,"Diamonds"), Card(4,"Spades"), Card(4,"Clubs"),
        Card(5,"Hearts"), Card(5,"Diamonds"), Card(5,"Spades"), Card(5,"Clubs"),
        Card(6,"Hearts"), Card(6,"Diamonds"), Card(6,"Spades"), Card(6,"Clubs"),
        Card(7,"Hearts"), Card(7,"Diamonds"), Card(7,"Spades"), Card(7,"Clubs"),
        Card(8,"Hearts"), Card(8,"Diamonds"), Card(8,"Spades"), Card(8,"Clubs"),
        Card(9,"Hearts"), Card(9,"Diamonds"), Card(9,"Spades"), Card(9,"Clubs"),
        Card(10,"Hearts"), Card(10,"Diamonds"), Card(10,"Spades"), Card(10,"Clubs"),
        Card(11,"Hearts"), Card(11,"Diamonds"), Card(11,"Spades"), Card(11,"Clubs"),
        Card(12,"Hearts"), Card(12,"Diamonds"), Card(12,"Spades"), Card(12,"Clubs"),
        Card(13,"Hearts"), Card(13,"Diamonds"), Card(13,"Spades"), Card(13,"Clubs"),
        Card(1,"Hearts"), Card(1,"Diamonds"), Card(1,"Spades"), Card(1,"Clubs")]