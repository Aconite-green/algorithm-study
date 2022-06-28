# Euclidean algorithm

def gcd(x: int, y: int) -> int:
    if y ==0:
        return x
    else:
        return gcd(y, x%y)

# math.gcd() can do the same thing