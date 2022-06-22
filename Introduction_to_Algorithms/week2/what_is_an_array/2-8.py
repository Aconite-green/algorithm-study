counter = 0

for n in range(2, 20):
    for i in range(2, n):
        counter += 1
        if n % i ==0:
            break
    else:
        print(n)

print(f'how many counts? : {counter}')