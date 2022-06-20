# + and - to print alternately

n = int(input('number of +, - ? :'))

for i in range(n):
    if i%2 == 0:
        print('-',  end="")
    else:
        print('+', end="")

# problems
# 1.always running if statments by for loop
# 2.difficult to change
        