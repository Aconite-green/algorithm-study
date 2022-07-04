# Searching for a string using the brute force method

def bf_match(txt: str, pat: str) -> int:
    
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == "__main__":
    s1 = input('type text: ')
    s2 = input('type patterns: ')

    idx = bf_match(s1, s2)

    if idx == -1:
        print('no patterns in text')
    else:
        print(f'at {idx + 1} these are patterns')

    # string search library
    # find, rfind, index, rindex