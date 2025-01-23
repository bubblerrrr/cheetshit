m, n, p, q = map(int, input().split())
juzhen = []
juanjihe = []
for _ in range(m):
    w = [int(i) for i in input().split()]
    juzhen.append(w)
for _ in range(p):
    w = [int(i) for i in input().split()]
    juanjihe.append(w)
i = 0
j = 0
all_result=[]
while i <= m - p and j <= n - q:
    result = []
    current = 0
    for o in range(i, i + p):
        for b in range(j, j + q):
            current += juzhen[o][b] * juanjihe[o - i][b - j]
    if j == n - q:
        all_result.append(result[:])
        j = 0
        i += 1
    elif j != n - q:
        j += 1
        result.append(current)
for i in all_result:
    print(*i)