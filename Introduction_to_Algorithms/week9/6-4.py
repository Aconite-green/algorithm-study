# Algorithm improvement2(bubble sort)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n-1:
        last = n -1
        