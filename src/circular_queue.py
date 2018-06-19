from collections import deque


class CircularQueue(deque):
    def popleft(self):
        popped = super(CircularQueue, self).popleft()
        self.append(popped)
        return popped
