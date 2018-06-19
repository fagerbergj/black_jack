import sys, os
import pytest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

from circular_queue import CircularQueue


class TestCircularQueue(object):

    def test_pop_puts_element_to_back_of_queue(self):
        queue = CircularQueue()
        queue.append("4")
        queue.append("5")
        popped = queue.popleft()
        
        assert popped == "4"
        assert list(queue) == ["5", "4"]
