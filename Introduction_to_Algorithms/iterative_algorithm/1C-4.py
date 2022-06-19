# Learn Python Variables

# gloabal variable
n=1
def put_id():
    # local variable
    x = 1
    print(f'id(x) = {id(x)}')

print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()


