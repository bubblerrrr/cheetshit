from collections import Counter
from math import comb
def good_num(n,s):

    pianyiliang = [0] * (n + 1)
    count = 0

    def pianyi():
        new_s=[]
        b = [0]
        for i in range(len(s)):
            new_s.append(int(i))
        for i in range(1, len(s) + 1):
            b.append(sum(new_s[:i]))
            pianyiliang[i] = b[i] - i

    pianyi()
    a = Counter(pianyiliang)
    for i in a:
        if a[i] >=2:
            count += comb(a[i], 2)
    print(count)


nCase = int(input())
for _ in range(nCase):
    n=int(input())
    s=input()
    good_num(n,s)

    else:
        print(-1)


nCase = int(input())
for _ in range(nCase):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    www(a, x)