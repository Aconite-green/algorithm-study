# Output an isosceles triangle(bottom left)

n = int(input('type shortest length in triangle :'))

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()