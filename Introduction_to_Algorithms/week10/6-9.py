from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = 1

    while h < n//9:
        h = h*3+1
        
        while h > 0:
            for i in range(h, n):
                j = i - h
                tmp = a[i]
                while j >= 0 and a[j] > tmp:
                    a[j + h] = a[j]
                    j -= h
                    a[j + h] = tmp
            h //= 3

if __name__ == "__main__":
    print('start shell sort')
    num = int(input('num = '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]'))

        shell_sort(x)

    print('in ascening order')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


# Shell sort first divides the elements of the array to be sorted into groups, and sorts by each group. 
# A method to reduce the number of movement of elements by repeating the operation of merging the sorted groups after that