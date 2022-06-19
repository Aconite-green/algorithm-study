# List the lengths of sides in a rectangle of integer length and width

area = int(input('area of rectagle : '))

for i in range(1, area+1):
    if i*i > area: break
    if area % i : continue
    print(f'{i} * {area//i}')