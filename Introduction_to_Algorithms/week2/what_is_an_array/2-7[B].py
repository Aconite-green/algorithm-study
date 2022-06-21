from card_conv import card_conv

if __name__ == '__main__':
    print('convert decimal')

    while True:
        while True:
            no = int(input('type value :'))
            if no > 0:
                break

        while True:
            cd = int(input('which decimal type? : '))

            if 2 <= cd <= 36:
                break

        print(f'in {cd} the output is {card_conv(no, cd)}')

        retry = input('One more ?(Y----yes/N-----no : ')
        if retry in {'N', 'n'}:
            break
        

        

