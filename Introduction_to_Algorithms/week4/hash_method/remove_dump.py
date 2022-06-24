from __future__ import annotations
from typing import Any, Type
import hashlib
from chainedhash import ChainedHash
from node import Node

def remove(self, key: Any) -> bool:
    hash = self.hash_value(key)
    p = self.table[hash]
    pp = None

    while p is not None:
        if p.key == key:
            if pp is None:
                self.table[hash] = p.next
            else:
                pp.next = p.next
            return True
        pp = p
        p = p.next
    return False

def dump(self) -> None:
    for i in range(self.capacity):
        p = self.table[i]
        print(i, end='')
        while p is not None:
            print(f' -> {p.key} ({p.value})', end='')
            p = p.next
        print()