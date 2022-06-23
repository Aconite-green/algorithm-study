from ssearch_while import seq_search

print('print "End" to stop')

number = 0
x = []

while True:
    s = input(f'x[{number}] : ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

ky = float(input('which value you want to search? : '))

idx = seq_search(x, ky)
if idx == -1:
    print('no valid element')
else:
    print(f'value is at x[{idx}]')