# python3
import sys

def myfunc(s):
    return s[0]

def lex_sort(M):
    A = M
    A.sort(key=myfunc)
    return A

def BWT(string):
    M = []
    n = {'$':1, 'A':2, 'C':3, 'G':4, 'T':5}

    for i in range(len(string)):
        num = 0
        st = string[i::]+string[0:i:]
        for j in range(len(st)):
            num = num*10 + n[st[j]]
        M.append((num,string[i::]+string[0:i:]))

    M = lex_sort(M)
    bwt = ''
    for p in M:
        bwt+=(p[1][-1])

    return bwt

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    #text = input()
    print(BWT(text))
