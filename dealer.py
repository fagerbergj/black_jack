from .deck import Deck

class Dealer():
    def __init__(self, name, house_money, deck, hand):
        self.name = name
        self.house_money = house_money
        self.deck = deck
        self.hand = hand

    def draw(self, target):
        target.hand.append(self.deck.draw())