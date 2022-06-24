from enum import Enum
from chainedhash import ChainedHash
from node import Node
from remove_dump import remove, dump
from search_add import search, add

Menu = Enum('Menu', ['add', 'remove', 'search', 'dump', 'end'])

def select_menu() -> Menu:

    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1<= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = int(input('put key you want to add: '))
        val = input('value: ')
        if not hash.add(key, val):
            print('fail to add')

    elif menu == Menu.remove:
        key = int(input('put key you want to remove: '))
        if not hash.remove(key):
            print('fail to remove')

    
    elif menu == Menu.search:
        key = int(input('put key you want to search: '))
        t = hash.search(key)
        if t is not None:
            print(f'the value {t} is the one you want to find')
        else:
            print('no data')

    elif menu == Menu.dump:
        hash.dump()

    else:
        break
