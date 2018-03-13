class Player():
    def __init__(self, name, money, hand=[]):
        self.name = name
        self.money = money
        self.hand = hand

    def status(self):
         print("Player's Remaining Money: {}\n Player Hand: {}".format(self.money, self.hand))