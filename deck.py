from random import shuffle

class Deck():
    def __init__(self, cards):
        self.cards = cards
    
    def draw(self):
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card

    def shuffle(self):
        self.cards = shiffle(cards)