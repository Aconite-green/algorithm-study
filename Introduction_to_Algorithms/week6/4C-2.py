# ring buffer

n = int(input('n : ?'))
a = [None] * n

cnt=0
while True:
    a[cnt % n] = int(input(f'type {cnt+1}"s number'))
    cnt += 1

    retry = input(f'continue?(Y-----yes / N ------- no')
    if retry in {'N', 'n'}:
        break

i = cnt-n
if i< 0: i=0

while i < cnt:
    print(f'{i+1}"s = {a[i% n]}')
    i += 1