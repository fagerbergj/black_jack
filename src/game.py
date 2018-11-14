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

    def deal_cards(self):
        print("\n........DEALING CARDS........")
        self.dealer.draw(self.player)
        self.dealer.draw(self.player)
        self.player.status()
        self.dealer.draw()
        self.dealer.status()

    def do_player_input(self):
        move = input("Move Options: \nh = hit\ns = stay\nd = double\nsp = split\nEnter move:")
        while(not self.cur_player.is_valid_move(move)):
            move = input("MOVE INVALID\nEnter move:")
        self.player_move(move)
        self.cur_player.status()
        self.cur_player.curr_hand.sum()

    def is_game_over(self):
        return self.dealer.house_money <= 0 or self.player.money <= 0

    def place_bet(self):
        if (isinstance(self.cur_player, Player)):
            valid_bet = self.cur_player.get_valid_bet(self.min)
            self.cur_player.bet(valid_bet)

    def init_round(self):
        self.cur_player = self.turn_manager.popleft()
        self.place_bet()
        self.deal_cards()
    
    def do_round(self):
        print("\n........TURNS........")
        while(isinstance(self.cur_player, Player)):
            try:
                move = None
                while(move != 's' and move != 'd'):
                    self.do_player_input()
            except HandBustException:
                print("BUST")
                pass
            self.cur_player.curr_bet = 0
            self.cur_player = self.turn_manager.popleft()

            self.cur_player.move()

    def run(self):
        print("........GAME HAS STARTED........\n")
        while not self.is_game_over():
            self.init_round()
            self.do_round()

            #win con detection
            #payouts
            return