from typing import Any, Sequence
import copy
def seq_search(seq : Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(seq) else i

if __name__ == "__main__":
    num = int(input('type the number of elements : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

ky = int(input('the value you search :'))

idx = seq_search(x, ky)

if idx == -1:
    print('not found')
else:
    print(f'its is x[{idx}]')

