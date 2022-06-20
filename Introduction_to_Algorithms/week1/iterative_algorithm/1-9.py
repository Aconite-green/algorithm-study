# get sum of a to b

a = int(input('value of a : '))
b = int(input('value of b : '))

if a > b:
    a,b = b,a

sum = 0
for i in range(a, b+1):
    sum +=i
    
# sequence of changing to value(line 6)
# b,a -> make tuple (b, a) -> unwrap tuple summit to variables a and b