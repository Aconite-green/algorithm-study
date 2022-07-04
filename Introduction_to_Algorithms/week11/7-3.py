# Searching for Strings Using the Boyer-Moor Method

# Starts at the end of the pattern and checks forward. If a character that does not match is found during this process, 
# the value to which the pattern moves is determined based on a table prepared in advance

def bm_match(txt: str, pat: str) -> int:
    skip = [None] * 256

    # make skip table
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # search
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp  else len(pat) - pp
             

    return -1

if __name__ == "__main__":
    s1 = input('type text: ')
    s2 = input('type patterns: ')

    idx = bm_match(s1, s2)

    if idx == -1:
        print('no patterns in text')
    else:
        print('oh yes')
