from dealer import Dealer
from player import Player
from deck import Deck

class Game():
    def __init__(self):
        self.dealer = Dealer(input("Dealer Name: "), int(input("House Limit: ")))
        self.player = Player(input("Player Name: "), int(input("Player Limit: ")))

        exit_condition = self.dealer.house_money <= 0 or self.player.money <= 0
        while not exit_condition:
            #Deal Cards
            print("Dealing Cards.........")
            self.dealer.draw(self.player)
            self.dealer.draw(self.player)
            self.player.status()
            self.dealer.draw()
            self.dealer.status()
            return
            #Check hands
            #player decides moves
            #winner is determined
            #money is shifted
            #player decides if they want to leave