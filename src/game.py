from dealer import Dealer
from player import Player
from deck import Deck
from circular_queue import CircularQueue


class HandBustException(Exception):
    pass


class Game():
    def __init__(self):
        print("\n........HOUSE VARIABLES........")
        self.dealer = Dealer(int(input("House Limit: ")))
        self.min = int(input("Enter table min: "))
        print("\n........PLAYER VARIABLES........")
        self.player = Player(input("Player Name: "), int(input("Player Limit: ")))

        #Turn manager
        self.turn_manager = CircularQueue()
        self.turn_manager.append(self.player)
        self.turn_manager.append(self.dealer)

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
        if len(sums) == 0:
            raise HandBustException
        return sums

    def filter_out_busts(self, sums):
        r = set()
        for s in sums:
            if s <= 21:
                r.add(s)
        return r
    
    def get_valid_bet(self, name):
        bet = int(input("{} place your bet: ".format(name)))
        if bet > self.player.money:
            print("Invalid bet, bet too high")
            return self.get_valid_bet(name)
        elif bet < self.min:
            print("Invalid bet, bet too low")
            return self.get_valid_bet(name)
        else:
            return bet

    def is_valid_move(self, i):
        return i == "h" or i == "s"
    
    def player_move(self, i):
        if i == "h":
            self.hit(self.player)
        elif i == "s":
            self.stay()

    def hit(self, player):
        self.dealer.draw(player)

    def stay(self):
        pass

    def start(self):
        exit_condition = self.dealer.house_money <= 0 or self.player.money <= 0
        print("........GAME HAS STARTED........\n")
        while not exit_condition:
            cur_player = self.turn_manager.popleft()

            if(isinstance(cur_player, Player)):
                cur_player.bet(self.get_valid_bet(self.player.name))
            #Deal Cards
            print("\n........DEALING CARDS........")
            self.dealer.draw(self.player)
            self.dealer.draw(self.player)
            self.player.status()
            self.dealer.draw()
            self.dealer.status()

            print("\n........TURNS........")

            while(isinstance(cur_player, Player)):
                try:
                    move = None
                    while(move != 's'):
                        move = input("Move Options: \nh = hit\ns = stay\nEnter move:")
                        while(not self.is_valid_move(move)):
                            move = input("MOVE INVALID\nEnter move:")
                        self.player_move(move)
                        cur_player.status()
                        self.sum_hand(cur_player.hand)
                except HandBustException:
                    print("BUST")
                    pass
                cur_player = self.turn_manager.popleft()

            #dealer moves until >17 or bust
            try:
                while(max(self.sum_hand(cur_player.hand)) <= 17):
                    self.hit(cur_player)
                    cur_player.status()
            except HandBustException:
                pass

            #win con detection
            #payouts
            return