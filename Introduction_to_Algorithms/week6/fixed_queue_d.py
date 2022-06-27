from fixed_queue_a import *
from fixed_queue_bc import *

def peek(self) -> Any:

    if self.is_empty():
        raise FixedQuene.Empty
    return self.que[self.front]

def find(self, value: Any) -> Any:
    for i in range(self.no):
        idx = (i+self.front) % self.capacity
        if self.que[idx] == value:
            return idx
        return -1

def count(self, value: Any) -> bool:
    c = 0
    for i in range(self.no):
        idx = (i+self.front) % self.capacity
        if self.que[idx] == value:
            c += 1
    return c

def __contains__(self, value: Any) -> bool:
    return self.count(value)

def clear(self) -> None:
    self.no = self.front = self.rear =0

def dump(self) -> None:
    if self.is_empty():
        print("q is empty")
    else:
        for i in range(self.no):
            print(self.que[(i+self.front) % self.capacity], end='')
        print()
