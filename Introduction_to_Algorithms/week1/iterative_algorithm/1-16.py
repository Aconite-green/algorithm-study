# Find the sum of integers from 1 to n (n is a positive number)

while True:
    n = int(input('n :'))
    if n >0 :
        break

sum=0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1

print(f'sum of integers from 1 to n is {sum}')