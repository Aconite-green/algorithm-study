# Print Maximum Value of Sequence Elements

from typing import Any, Sequence

def max_of(a : Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximu = a[i]
    return maximum

if __name__ == '__main__':
    print('get maximum in array')
    num = int(input('number of element? :'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'put the value of x[{i}]'))

    print(f'maximum is {max_of(x)}')

    # scan, traverse : A method of paying attention to the non-thermal elements one by one
    # module : one script program(ex max.py -> max)
    # Sequuence type : list, bytearry ,str, tuple, bytes