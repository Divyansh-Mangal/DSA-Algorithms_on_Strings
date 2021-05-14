# python3
import sys
def PrefixFunc(P):
    s = [0]*len(P)
    border = 0
    n = 0
    for i in range(1,len(s)):
        while border > 0 and P[i] != P[border]:
            border = s[border-1]
        if P[i] == P[border]:
            border += 1
        else:
            border = 0
        s[i] = border

    return s

def find_pattern(P, T):
    string = P+'$'+T
    prefix = PrefixFunc(string)
    sizeP = len(P)

    pos = []
    for i in range(sizeP+1,len(prefix)):
        if prefix[i] == sizeP:
            pos.append(i-2*sizeP)
    return pos


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))
