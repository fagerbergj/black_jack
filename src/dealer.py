from deck import Deck

class Dealer():
    def __init__(self, house_money, hand=[], deck=Deck()):
        self.house_money = house_money
        self.deck = deck
        self.hand = hand

    def draw(self, target=None):
        if(len(self.deck.cards) == 0):
            self.deck = Deck()
        if(target == None):
            self.hand.append(self.deck.draw())
            return
        
        target.curr_hand.append(self.deck.draw())

    def status(self):
        print("Dealer's Remaining Money: {}\n Dealer Hand: {}".format(self.house_money, self.hand))