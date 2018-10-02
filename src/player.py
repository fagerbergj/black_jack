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