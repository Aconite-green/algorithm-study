def recur(n: int) -> int:
    if n >0:
        recur(n - 1)
        print(n)
        recur(n - 2)

    x = int(input('x : '))
    
    recur(x)

    # Top-down analysis is an analysis method that starts with a function call in the topmost box and goes through the details step by step.
    # Contrary to top-down analysis, it is a method of analyzing from the bottom up.