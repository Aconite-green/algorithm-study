def med3_1(a,b,c):
    if a>=b:
        if b>= c:
            return b
        elif c <= a:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

    
def med3_2(a,b,c,):
    if (b >= a and c <= a) or (b >= a and c <= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

# med3_2 is not effitient as med3_1, 
# because at line 18, 20 there is duplicated comparison(with a and b)