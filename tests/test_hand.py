import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

import pytest

from card import Card
from hand import Hand, HandBustException


class TestHand(object):

    def test_sum_no_ace(self):
        h = Hand([Card(10, "Hearts"), Card(2, "Clubs")])
        assert h.sum() == {12}

    def test_sum_has_ace(self):
        h = Hand([Card(8, "Hearts"), Card("Ace", "Clubs")])
        assert h.sum() == {19,9}

    def test_sum_has_multi_ace(self):
        h = Hand([Card(8, "Hearts"), Card("Ace", "Clubs"), Card("Ace", "Clubs")])
        assert h.sum() == {10,20}

    def test_sum_worst_case(self):
        h = Hand([Card("Ace", "Clubs")] * 16)
        assert h.sum() == {16}

    def test_sum_equals_21(self):
        h = Hand([Card("Ace", "Clubs"), Card(10, "Clubs")])
        assert h.sum() == {11, 21}

    def test_sum_raises_bust_exception(self):
        h = Hand([Card("Ace", "Clubs"), Card("Jack", "Clubs"), Card("Queen", "Clubs"), Card(4, "Clubs")] )
        with pytest.raises(HandBustException):
            h.sum()