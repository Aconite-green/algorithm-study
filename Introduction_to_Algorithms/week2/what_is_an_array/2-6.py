# Sort the elements of the mutable sequence in reverse order

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[i-n-1] = a[i-n-1], a[i]

if __name__ == '__main__':
    nx = int(input('number of element :'))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}] = '))

    reverse_array(x)

    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

    # y = list(reversed(x))