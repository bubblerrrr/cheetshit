# 滑雪
#返回值型DFS
# 创造一个矩阵表示某个点最多产生的路径数
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
m, n = map(int, input().split())
maze = []
dp=[[0 for _ in range(n)] for _ in range(m)]
for _ in range(m):
    maze.append(list(map(int, input().split())))


def is_valid(x, y):
    if 0 <= x < m and 0 <= y < n:
        return True
    return False


def dfs(x, y):
    if dp[x][y]!=0:
        return dp[x][y]
    dp[x][y]=1
    for dx, dy in dir:
        if is_valid(x + dx, y + dy):
            if maze[x + dx][y + dy] < maze[x][y]:
                dp[x][y]= max(1+dfs(x+dx,y+dy),dp[x][y])
    return dp[x][y]

zuichang=0
for i in range(m):
    for j in range(n):
        zuichang=max(dfs(i, j),zuichang)
print(zuichang)