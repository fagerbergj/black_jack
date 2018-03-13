from deck import Deck

class Dealer():
    def __init__(self, name, house_money, hand=[], deck=Deck()):
        self.name = name
        self.house_money = house_money
        self.deck = deck
        self.hand = hand

    def draw(self, target=None):
        if(target == None):
            target = self
        if(len(self.deck.cards ) == 0):
            self.deck = Deck()
        target.hand.append(self.deck.draw())

    def status(self):
        print("Dealer's Remaining Money: {}\n Dealer Hand: {}".format(self.house_money, self.hand))