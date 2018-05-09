class Player():
    def __init__(self, name, money, hand=[]):
        self.name = name
        self.money = money
        self.hand = hand

    def status(self):
        print("Player's Remaining Money: {}\n Player Hand: {}".format(self.money, self.hand))

    def bet(self):
        bet = int(input("Place your bets: "))
        if bet > self.money:
            print("Invalid bet, bet too high")
            self.bet()
        else:
            self.money -= bet