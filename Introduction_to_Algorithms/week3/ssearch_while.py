# Linear Search Algorithm

from typing import Any, Sequence

def seq_search(a : Sequence, key : Any) -> int :
    i =0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

if __name__ == '__main__':
    num = int(input('num : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] '))

    ky = int(input('the value you want to search :'))

    idx = seq_search(x, ky)

    if idx == -1:
        print('fail')
    else:
        print(f'the value is in x[{idx}]')