from dealer import Dealer
from player import Player
from deck import Deck

class Game():
    def __init__(self):
        self.dealer = Dealer(input("Dealer Name: "), int(input("House Limit: ")))
        self.player = Player(input("Player Name: "), int(input("Player Limit: ")))

    def sum_hand(self, h):
        base_sum = 0
        aces = []
        res = set()

        for c in h:
            if c.value != (1,11):
                base_sum += c.value
            else:
                aces.append(c)
        
        if not aces:
            return {base_sum}

        for a in aces:
            for v in a.value:
                res.add(base_sum + v)

        return res

    def start(self):
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
