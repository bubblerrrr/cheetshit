n = int(input())
s = [[1] * (n + 2)]
N = s + [[1] + [0] * n + [1]for _ in range(n)] + s
row = 1
col = 1
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = 0
dx, dy = direction[count % 4][0], direction[count % 4][1]
for i in range(1, n * n + 1):
    N[row][col] = i
    if N[row + dx][col + dy]:
        count += 1
        dx, dy = direction[count % 4][0], direction[count % 4][1]
    row += dx
    col += dy
for i in range(1, n + 1):
    print(*N[i][1:-1])