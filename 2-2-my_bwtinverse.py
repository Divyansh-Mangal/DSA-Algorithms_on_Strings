# python3
import sys

def InverseBWT(bwt):
    countBWT = {'$':[], 'A':[], 'C':[], 'G':[], 'T':[]}
    bwtList = []

    for i in range(len(bwt)):
        countBWT[bwt[i]].append(i)

    order = []
    for ch in ['$','A','C','G','T']:
        order += countBWT[ch]



    inv = ''
    i = order[order[0]]
    while i != order[0]:
        inv+=bwt[i]
        i = order[i]

    return inv+'$'


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    #bwt = input()
    print(InverseBWT(bwt))
