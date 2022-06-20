n = int(input('n :'))

for _ in range(n//2):
    print('+-', end="")

if n%2:
    print('+', end="")

print()

# _ : not using value = dont't care
# come pare to 1-12.py more efficent and easy to change
