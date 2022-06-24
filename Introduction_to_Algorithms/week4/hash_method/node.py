from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


# hashing : Finding the location to store data with a simple operation
# hash function : The process of converting a key (element value) into a hash value
# bucket : Elements created from hashtables
# collision : Duplicate storage buckets