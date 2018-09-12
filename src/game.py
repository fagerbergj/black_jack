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
        self.cur_player = self.turn_manager[0]

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
    
    def get_valid_bet(self):
        bet = int(input("{} place your bet: ".format(self.player.name)))
        if bet > self.player.money:
            print("Invalid bet, bet too high")
            return self.get_valid_bet()
        elif bet < self.min:
            print("Invalid bet, bet too low")
            return self.get_valid_bet()
        else:
            return bet

    def is_valid_move(self, i):
        if i == "sp":
            has_same_val = self.player.curr_hand[0].value  == self.player.curr_hand[1].value
            has_enough_money = self.player.curr_bet <= self.player.money
            return len(self.player.curr_hand) == 2 and has_same_val and has_enough_money
        if i == "d":
            return self.player.curr_bet <= self.player.money
        return i == "h" or i == "s"
    
    def player_move(self, i):
        if i == "h":
            self.hit()
        elif i == "s":
            self.stay()
        elif i == "d":
            self.double()
        

    def hit(self):
        self.dealer.draw(self.cur_player)

    def stay(self):
        pass

    def double(self):
        self.player.bet(self.player.curr_bet)
        self.hit()

    def start(self):
        exit_condition = self.dealer.house_money <= 0 or self.player.money <= 0
        print("........GAME HAS STARTED........\n")
        while not exit_condition:
            self.cur_player = self.turn_manager.popleft()

            if(isinstance(self.cur_player, Player)):
                self.cur_player.bet(self.get_valid_bet())
            #Deal Cards
            print("\n........DEALING CARDS........")
            self.dealer.draw(self.player)
            self.dealer.draw(self.player)
            self.player.status()
            self.dealer.draw()
            self.dealer.status()

            print("\n........TURNS........")
            while(isinstance(self.cur_player, Player)):
                try:
                    move = None
                    while(move != 's' and move != 'd'):
                        move = input("Move Options: \nh = hit\ns = stay\nd = double\nsp = split\nEnter move:")
                        while(not self.is_valid_move(move)):
                            move = input("MOVE INVALID\nEnter move:")
                        self.player_move(move)
                        self.cur_player.status()
                        self.sum_hand(self.cur_player.curr_hand)
                except HandBustException:
                    print("BUST")
                    pass
                self.cur_player.curr_bet = 0
                self.cur_player = self.turn_manager.popleft()

            #dealer moves until >17 or bust
            try:
                while(max(self.sum_hand(self.cur_player.curr_hand)) <= 17):
                    self.hit()
                    self.cur_player.status()
            except HandBustException:
                pass

            #win con detection
            #payouts
            return