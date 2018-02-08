from card import Card

class TestCard():
    def test_card(self):
        test = Card(11,"Spades")
        assert test.value == 11
        assert test.suit == "Spades"
    
    def test_to_string(self):
        jack = Card(11,"Hearts")
        queen = Card(12,"Spades")
        king = Card(13, "Diamonds")
        ace = Card(1, "Clubs")
        num = Card(6, "Hearts")
        assert str(jack) == "Jack of Hearts"
        assert str(queen) == "Queen of Spades"
        assert str(king) == "King of Diamonds"
        assert str(ace) == "Ace of Clubs"
        assert str(num) == "6 of Hearts"



