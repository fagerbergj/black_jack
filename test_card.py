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
     

    def test_compare(self):
        jack = Card(11,"Hearts")
        queen = Card(12,"Spades")
        king = Card(13, "Diamonds")
        ace = Card(1, "Clubs")
        six = Card(6, "Hearts")
        five = Card(5, "Hearts")

        assert jack == Card(11,"Hearts")
        assert jack == Card(11,"Clubs")
        assert jack != queen

        assert jack < ace
        assert not king < queen
        assert not jack < jack

        assert six > five
        assert not five > queen
        assert not queen > queen

    def test_same_as(self):
        t1 = Card(11,"Hearts")
        t2 = Card(11,"Clubs")
        t3 = Card(9,"Hearts")
        t4 = Card(9,"Clubs")
        t5 = Card(11,"Hearts")

        assert t1.same_as(t5)
        assert not t1.same_as(t2)
        assert not t1.same_as(t3)
        assert not t1.same_as(t4)

