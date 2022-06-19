# Print * n times with a newline at number of w

n = int(input('n :'))
w = int(input('w :'))

for i in range(n):
    print('*', end='')
    if i%w == w-1:
        print()

# problems
# 1.use if statement everytimes by for loop