# put three value , get maximum

print('get maximum')
a = int(input('type value of a:'))
b = int(input('type value of b:'))
c = int(input('type value of c:'))


maximum = a
if maximum < b: maximum = b
if maximum < c: maximum = c
print(f'maximum is {maximum}')

# 1.above code is squential structure, because it runs from the top to the bottom in sequence
# 2.above code is select structure, because it uses 'if' statement(selection method)
# 3.if, while -> header