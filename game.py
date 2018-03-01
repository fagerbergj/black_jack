from black_jack.dealer import Dealer
from black_jack.player import Player
from black_jack.deck import Deck

class Game():
    def __init__(self):
        self.dealer = Dealer(input("Dealer Name: "), input("House Limit: "), Deck(), [])
        self.player = Player(input("Player Name: "), input("Player Limit: "), [])