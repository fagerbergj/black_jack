from dealer import Dealer
from player import Player
from deck import Deck

class Game():
    def __init__(self):
        self.dealer = Dealer(input("Dealer Name: "), int(input("House Limit: ")))
        self.player = Player(input("Player Name: "), int(input("Player Limit: ")))
        self.min = int(input("Enter table min: "))

    def sum_hand(self, h):
        base_sum = 0
        aces = 0
        res = set()

        for c in h:
            if c.value != (1,11):
                base_sum += c.value
            else:
                aces += 1

        return self.get_sums(aces, base_sum)

    def get_sums(self, aces, base_sum):
        
        height_of_heap = (2**(aces + 1) - 1)
        val_heap = [0] * height_of_heap
        val_heap[0] = base_sum

        return_length = (2**(aces) - 1)
        for i in range(return_length):
            val_heap[2*i + 1] = val_heap[i] + 1
            val_heap[2*i + 2] = val_heap[i] + 11

        raw_sums = {*val_heap[return_length:]}
        sums = self.filter_out_busts(raw_sums)
        return sums

    def filter_out_busts(self, sums):
        r = set()
        for s in sums:
            if s <= 21:
                r.add(s)
        return r
    
    def get_valid_bet(self):
        bet = int(input("Place your bets: "))
        if bet > self.player.money:
            print("Invalid bet, bet too high")
            return self.get_valid_bet()
        elif bet < self.min:
            print("Invalid bet, bet too low")
            return self.get_valid_bet()
        else:
            return bet


    def start(self):
        exit_condition = self.dealer.house_money <= 0 or self.player.money <= 0
        while not exit_condition:
            self.player.bet(self.get_valid_bet())
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
