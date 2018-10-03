from hand import Hand

class Player():
    def __init__(self, name, money, hand=Hand()):
        self.name = name
        self.money = money
        self.curr_hand = hand
        self.curr_bet = 0

    def status(self):
        print("Player's Remaining Money: {}\n Player Hand: {}".format(self.money, self.curr_hand))

    def bet(self, b):
        self.curr_bet += b
        self.money -= b

    def get_valid_bet(self, table_min):
        bet = int(input("{} place your bet: ".format(self.name)))
        if bet > self.money:
            print("Invalid bet, bet too high")
            return self.get_valid_bet(table_min)
        elif bet < table_min:
            print("Invalid bet, bet too low")
            return self.get_valid_bet(table_min)
        else:
            return bet