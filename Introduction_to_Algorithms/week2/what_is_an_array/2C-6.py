def change(lst, idx, val):
    lst[idx] = val

x = [11, 22, 33, 44, 55]
print('x=', x)

index = int(input('idx = '))
value = int(input('val = '))

change(x, index, value)
print(f'x = {x}')

# When an argument is immutable
# Changing the value of a parameter inside a function creates another object and updates it with a reference to that object. 
# Therefore, changing the parameters of the parameters does not affect the actual arguments of the caller.

# When an argument is mutable
# Changing the value of a parameter inside a function updates the object itself. 
# So, changing the value of a parameter changes the value of the actual argument on the calling side.
