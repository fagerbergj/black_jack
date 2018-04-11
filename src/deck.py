from random import shuffle
from card import Card

class Deck():
    def __init__(self, *args):
        if not args:
            self.default_deck()
        else:
            self.cards = args[0]
    
    def draw(self):
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card

    def size(self):
        return len(self.cards)

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
        Card("Jack","Hearts"), Card("Jack","Diamonds"), Card("Jack","Spades"), Card("Jack","Clubs"),
        Card("Queen","Hearts"), Card("Queen","Diamonds"), Card("Queen","Spades"), Card("Queen","Clubs"),
        Card("King","Hearts"), Card("King","Diamonds"), Card("King","Spades"), Card("King","Clubs"),
        Card("Ace","Hearts"), Card("Ace","Diamonds"), Card("Ace","Spades"), Card("Ace","Clubs")] * 4
        self.shuffle()