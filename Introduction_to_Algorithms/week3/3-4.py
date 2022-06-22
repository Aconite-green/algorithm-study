# Binary Search Algorithm

from typing import Sequence, Any

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl+pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc+1
        else:
            pr = pc - 1
        
        if pl > pr:
            break
        return -1

if __name__ == "__main__":
    num = int(input('num :'))
    x = [None] * num

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))        
            if x[i] >= x[i-1]:
                break

    ky = int(input('key : '))
    idx = bin_search(x, ky)

    if idx == -1:
        print('no element')
    else:
        print(f'its in x[{idx}]')
