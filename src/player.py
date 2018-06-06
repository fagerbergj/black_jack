class Player():
    def __init__(self, name, money, hand=[]):
        self.name = name
        self.money = money
        self.hand = hand
        self.curr_bet = 0

    def status(self):
        print("Player's Remaining Money: {}\n Player Hand: {}".format(self.money, self.hand))

    def bet(self, b):
        self.curr_bet = b
        self.money -= b