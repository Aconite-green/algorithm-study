from fixed_stack_a import FixedStack
from fixed_stack_b import *
from typing import Any

def find(self, value: Any) -> Any:

    for i in range(self.ptr -1, -1, -1):
        if self.stk[i] ==value:
            return i
        return -1

def count(self, value: Any) -> bool:
    c=0
    for i in range(self.ptr):
        if self.stk[i] == value:
            c += 1
            
    return c



def __contains__(self, value: Any) -> bool:
    return self.count(value)

def dump(self) -> None:
    if self.is_empty():
        print('stack is empty')
    else:
        print(self.stk[:self.ptr])
