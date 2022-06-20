# get sum of 1 to  n(using while)

n = int(input('put the value of n'))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'sum of 1 to n is {sum}')