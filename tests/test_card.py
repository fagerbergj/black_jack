import sys, os
import pytest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

from card import Card

class TestCard():
    def test_card(self):
        test = Card("King","Spades")
        assert test.value == 10
        assert test.suit == "Spades"

    def test_invalid_card(self):
        with pytest.raises(ValueError) as e:
            test = Card(12, "Spades")
        assert "Card of value: 12 is not valid" in str(e)

        with pytest.raises(ValueError) as e:
            test = Card(8, "Poop")
        assert "Suit: Poop is not valid" in str(e)

    
    def test_to_string(self):
        jack = Card("Jack","Hearts")
        queen = Card("Queen","Spades")
        king = Card("King", "Diamonds")
        ace = Card("Ace", "Clubs")
        num = Card(6, "Hearts")
        assert str(jack) == "Jack of Hearts"
        assert str(queen) == "Queen of Spades"
        assert str(king) == "King of Diamonds"
        assert str(ace) == "Ace of Clubs"
        assert str(num) == "6 of Hearts"
     
    def test_repr(self):
        jack = Card("Jack","Hearts")
        queen = Card("Queen","Spades")
        king = Card("King", "Diamonds")
        ace = Card("Ace", "Clubs")
        num = Card(6, "Hearts")
        assert repr(jack) == "Jack of Hearts"
        assert repr(queen) == "Queen of Spades"
        assert repr(king) == "King of Diamonds"
        assert repr(ace) == "Ace of Clubs"
        assert repr(num) == "6 of Hearts"

