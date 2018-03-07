from .dealer import Dealer
from .player import Player
from .deck import Deck

class Game():
    def __init__(self):
        self.dealer = Dealer(input("Dealer Name: "), input("House Limit: "), Deck(), [])
        self.player = Player(input("Player Name: "), input("Player Limit: "), [])