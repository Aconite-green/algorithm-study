def factorial(n: int) -> int:

    if n >0:
        return n*factorial(n-1)
    else:
        return 1

if __name__ =='__main__':
    n = int(input('n:'))
    print(f'{n} of factoral is {factorial(n)}')

    # direct recursive : How to call a function identical to itself
    # indirect recursive : not calling it self directly (a -> b -> a) 