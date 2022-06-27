from enum import Enum
from fixed_stack_a import *
from fixed_stack_b import *
from fixed_stack_c import *


Menu = Enum('Menu', ['push', 'pop', 'peek','search', 'dump', 'end'])

def select_menu() -> Menu:

    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1<= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    menu = select_menu()


    if menu == Menu.push:
        x = int(input('type data'))
        try:
            s.push()
        except FixedStack.Full:
            print('stack is full')
    
    elif menu == Menu.pop:
        try: 
            x = s.pop
            print(f'the data you pop{x}')
        except FixedStack.Empty:
            print('stack is empty')

    elif menu == Menu.peek:
        try:
            x = x.peek()
            print(f'the data you peek {x}')
        except FixedStack.Empty:
            print('stack is empty')

    elif menu == Menu.search:
        x = int(input('type the value you want to search: '))
        if x in s:
            print(f'count = {s.count(x)} the location of the front is{s.find(x)}')
        else:
            print('no data')

    elif menu == Menu.dump:
        s.dump()

    else:
        break
        

# The deque module allows a simple implementation of the stack.
# collection.deque is a container that implements a deck, a data structure that adds/remove elements from both the front and the end.
    
