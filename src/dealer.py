from deck import Deck
from hand import Hand, HandBustException

class Dealer():
    def __init__(self, house_money, hand=Hand(), deck=Deck()):
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

    def move(self):
        """dealer moves until >=17 or bust"""
        try:
            while(max(self.hand.sum()) < 17):
                self.draw()
                self.status()
        except HandBustException:
            pass

    def status(self):
        print("Dealer's Remaining Money: {}\n Dealer Hand: {}".format(self.house_money, self.hand))