from dealer import Dealer
from hand import HandBustException
from player import Player
from deck import Deck
from circular_queue import CircularQueue


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

            if (isinstance(self.cur_player, Player)):
                valid_bet = self.cur_player.get_valid_bet(self.min)
                self.cur_player.bet(valid_bet)
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
                        self.cur_player.curr_hand.sum()
                except HandBustException:
                    print("BUST")
                    pass
                self.cur_player.curr_bet = 0
                self.cur_player = self.turn_manager.popleft()

            #dealer moves until >17 or bust
            try:
                while(max(self.cur_player.curr_hand.sum()) <= 17):
                    self.hit()
                    self.cur_player.status()
            except HandBustException:
                pass

            #win con detection
            #payouts
            return