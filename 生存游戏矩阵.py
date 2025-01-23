# 先创造一个矩阵在外围加一圈死细胞
n, m = map(int, input().split())
original = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
result = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
juzhen = []
for _ in range(n):
    row = list(map(int, input().split()))
    juzhen.append(row)
for i in range(0, n):
    for j in range(0, m):
        original[i + 1][j + 1] = juzhen[i][j]



def neigh_life(row, col):
    num = original[row - 1][col - 1] + original[row - 1][col] + original[row - 1][col + 1] + original[row][col - 1] + \
          original[row][col + 1] + original[row + 1][col - 1] + original[row + 1][col] + original[row + 1][col + 1]
    if not original[row][col]:
        if num == 3:
            result[row][col] = 1
    if original[row][col]:
        if num < 2 or num > 3:
            result[row][col] = 0
        else:
            result[row][col] = 1


for i in range(1, n + 1):
    for j in range(1, m + 1):
        neigh_life(i, j)
for i in range(1, n + 1):
    print(*result[i][1:m + 1]