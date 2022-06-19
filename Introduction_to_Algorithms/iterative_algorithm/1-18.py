# Generate a random number between 10 and 99

import random

n = int(input('n:'))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=" ")
    if r ==13:
        print('end program')
        break
    else:
        print('finish')