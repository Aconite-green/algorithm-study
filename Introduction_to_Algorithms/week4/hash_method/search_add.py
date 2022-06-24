from __future__ import annotations
from typing import Any, Type
import hashlib
from chainedhash import ChainedHash
from node import Node

def search(self, key: Any) -> Any:
    hash = self.hash_value(key)
    p = self.table[hash]

    while p is not None:
        if p.key == key:
            return p.value
        p = p.next
    return None


def add(self, key: Any, value: Any) -> bool:
    hash = self.hash_value(key)
    p = self.table[hash]

    while p is not None:
        if p.key == key:
            return False
        p=p.next
            

    temp = Node(key, value, self.table[hash])
    self.table[hash] = temp
    return True

