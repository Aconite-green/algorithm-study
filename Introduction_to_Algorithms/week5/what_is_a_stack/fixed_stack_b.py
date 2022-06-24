from fixed_stack_a import FixedStack
from typing import Any

def push(self, value: Any) -> None:
    if self.is_full():
        raise FixedStack.Full
    self.stk[self.ptr] = value
    self.ptr += 1

def pop(self) -> Any:
    if self.is_empty():
        raise FixedStack.Empty
    self.ptr -= 1
    return self.stk[self.ptr]

def peek(self) -> Any:
    if self.is_empty():
        raise FixedStack.Empty
    return self.stk[self.ptr - 1]

def clear(self) -> None:
    self.ptr = 0

        