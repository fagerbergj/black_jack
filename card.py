VAULE_MAP = {11:"Jack", 12:"Queen", 1:"Ace", 13:"King"}
class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        str_value = VAULE_MAP.get(self.value, self.value)
        return "{} of {}".format(str_value, self.suit)