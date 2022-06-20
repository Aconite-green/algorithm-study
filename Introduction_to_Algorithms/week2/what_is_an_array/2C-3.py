# Scan all elements of list with enumerate() function (count from 1)


x = ['John', 'George', 'paul', 'Ringo']

for i, name in enumerate(x, start=1):
    print(f'{i} = {name}')


# enumerate(x, start=) -> start means set starting index