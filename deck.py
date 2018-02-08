from queue import Queue
from random import shuffle

class Deck():
    def __init__(self, cards):
        self.cards = Queue(shuffle(cards))
    
    def draw(self):
        return self.cards.get()