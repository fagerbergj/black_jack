VAULE_MAP = {11:"Jack", 12:"Queen", (1,11):"Ace", 13:"King"}
class Card():
    def __init__(self, value, suit):
        self.value = value
        self.name = value
        if self.value in VAULE_MAP:
            self.name = VAULE_MAP.get(self.value, self.value)
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.name, self.suit)

    def __repr__(self):
        return self.__str__()

    def same_as(self, other):
        return self.value == other.value and self.suit == other.suit
