from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]

if __name__ == '__main__':
    print('start bubble sort')
    num = int(input('type numbe of elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(X)

    print('sorted in acending order ')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')




# Sorting refers to the operation of arranging a set of data in a certain order according to the magnitude relationship of the item values.
# A stable sorting algorithm means that the order of elements with the same value is maintained even when sorted.
# internal sorting : This is the algorithm to use when all the data to be sorted can be stored in one array.
# external sorting : This algorithm is used when there is a lot of data to be sorted and cannot be stored in one array.
# buble sort : An algorithm that compares the magnitude relationship of two neighboring elements and repeats the exchange as needed

