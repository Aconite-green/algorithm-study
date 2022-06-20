from Introduction_to_Algorithms.week2.what_is_an_array.max import max_of
from max import max_of

number = 0
x = []

while True:
    s = input(f'put the value of x[{number}]')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'you put {number} of values')
print(f'maximum is {max_of(x)}')