ddef Test():
    n = int(input())
    jincheng = []
    for _ in range(n):
        start, end = map(int, input().split())
        jincheng.append((start, end))
    jincheng.sort(key=lambda x: x[1])
    count = 0
    i=0
    while i < len(jincheng):
        count += 1
        end = jincheng[i][1]
        i += 1
        while i < len(jincheng) and jincheng[i][0] <= end:
            i += 1
    print(count)
nCase = int(input())
for _ in range(nCase):
    Test()