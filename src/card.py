VAULE_MAP = {"Jack":10, "Queen":10, "Ace":(1,11), "King":10}
SUITS = {"Spades", "Clubs", "Diamonds", "Hearts"}
class Card():
    def __init__(self, name, suit):
        self.name = name
        if suit not in SUITS:
            raise ValueError("Suit: {} is not valid".format(suit))
        if isinstance(name, str):
            self.value = VAULE_MAP[self.name]
        elif isinstance(name, int) and name > 10:
            raise ValueError("Card of value: {} is not valid".format(name))
        else:
            self.value = name
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.name, self.suit)

    def __repr__(self):
        return self.__str__()