# Algorithm improvement1(bubble sort)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:

    n = len(a)
    for i in range(n - 1, i, -1):
        exchng = 0
        for j in range(n - 1, i, -1):
            if a[j -1] > a[j]:
                a[j -1], a[j] = a[j], a[j -1]
                exchng += 1
    
            if exchng == 0:
                break

