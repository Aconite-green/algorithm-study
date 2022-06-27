# A queue is a first-in-first-out structure in which data that is put in first is retrieved first.
# Adding data is called enqueue, and pulling data out is called dequeue.
# The side that retrieves data is called the front, and the side that puts data in is called the rear.

from typing import Any

class FixedQuene:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

        