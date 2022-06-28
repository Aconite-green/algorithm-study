# hanoi tower

def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no -1, x, 6-x-y)
    
    print(f'[{no}] : {x} to {y}')

    if no > 1:
        move(no-1, 6-x-y, y)

    