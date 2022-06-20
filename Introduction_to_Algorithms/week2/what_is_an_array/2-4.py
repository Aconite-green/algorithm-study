# Finding and printing the maximum value of an array element 
# (generating the element value as a random number)

import random
from max import max_of

num = int(input('number of random value : '))
lo = int(input('minimum : '))
hi = int(input('maximum : '))
x = [None] * num
for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'maximum of x is {max_of(x)}')


