from __future__ import annotations
from typing import Any, Type
import hashlib

class ChainedHash : 
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

# chaining(open hashing) : Connecting data with the same hash value into a chain-shaped linked list
# sha256() : Algorithm constructor to get the hash value of a given byte string
# encode() : create byte string
# hexdigest() : Fetch the hash value as a hexadecimal string
# isinstance() : first = the value of data, second = the data type you want to check (is it same?)