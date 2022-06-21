def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1

    return s

x = int(input('put a value of x :'))
print(f'from 1 to {x}, the sum is {sum_1ton(x)}')