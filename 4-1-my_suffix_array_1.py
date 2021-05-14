# python3
import sys

def SortCharacters(S):
    characters = []
    charDict = {}
    count = []

    for i in range(len(S)):
        if S[i] not in charDict.keys():
            charDict[S[i]] = [i]
        else:
            charDict[S[i]].append(i)

    count = list(charDict.keys())
    count.sort()

    order = []
    for c in count:
        order += charDict[c]

    return order

def CharClass(S, order):
    cls = [0]*len(order)

    prev = None
    n = -1

    for i in range(len(order)):
        l = S[order[i]]
        if prev != l:
            n+=1
            cls[order[i]] = n
            prev = l
        else:
            cls[order[i]] = n
            prev = l

    return cls

def Updateclass(newOrder, cls, L):
    n = len(newOrder)

    newcls = [-1]*n
    newcls[newOrder[0]] = 0

    for i in range(1,n):
        cur = newOrder[i]
        prev = newOrder[i-1]

        mid = (cur+L)
        midPrev = (prev+L)%n

        if cls[cur] != cls[prev] or cls[mid] != cls[midPrev]:
            newcls[cur] = newcls[prev] + 1
        else:
            newcls[cur] = newcls[prev]

    return newcls

def SortDouble(S, L , order, cls):
    value = []
    n = len(order)

    sortSecond = lambda o : cls[(o+L)%n]
    sortFirst = lambda o : cls[o]

    order.sort(key = sortSecond)
    order.sort(key = sortFirst)

    return order



def build_suffix_array(S):
    order = SortCharacters(S)
    cls = CharClass(S, order)
    L = 1

    while L < len(S):
        order = SortDouble(S, L, order, cls)
        cls = Updateclass(order, cls, L)
        L  = 2*L

    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    #text = input()
    print(" ".join(map(str, build_suffix_array(text))))
