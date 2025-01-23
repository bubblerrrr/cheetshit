`from functools import reduce
L, M = map(int, input().split())
result = []
for _ in range(M):
    a, b = map(int,input().split())
    h= {i for i in range(a, b + 1)}
    result.append(h)

fi_result = reduce(lambda x, y: x | y , result)
s = L +1- len(fi_result)
print(s)