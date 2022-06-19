a = int(input('a :'))
b = int(input('b :'))

if a > b:
    a,b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end="")

print(f'{b} = ', end="")
sum += b

print(sum)

# not using if statement
# reducing number of repetitions