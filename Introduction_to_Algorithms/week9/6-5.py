# --- shaker sort, bidirectional bubble sort, cocktail sort ----
# An alignment method that alternates the scan direction of a pass by moving the smallest element to the front in odd passes 
# and moving the largest element to the back in even passes

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:

    left = 0
    right = len(a)
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right) :
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last

