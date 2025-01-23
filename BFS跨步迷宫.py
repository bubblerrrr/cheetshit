#借助辅助visit集合标记已访问的点
from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 2), (0, -2), (2, 0), (-2, 0)]
n, m = map(int, input().split())
maze = [[1 for _ in range(m + 4)] for _ in range(n + 4)]
for i in range(2, n + 2):
    maze[i][2:-2] = list(map(int, input().split()))


def BFS(x, y):
    q = deque([(x, y, 0)])
    visit = set()
    visit.add((x, y))
    while q:
        x, y, step = q.popleft()
        if x == n + 1 and y == m + 1:
            return step
        for i in range(4, 6):
            dy = dir[i][1]
            if maze[x][y + dy] == 0 and maze[x][y + (dy // 2)] == 0 and (x, y + dy) not in visit:
                visit.add((x, y + dy))
                q.append((x, y + dy, step + 1))
        for i in range(6, 8):
            dx = dir[i][0]
            if maze[x + dx][y] == 0 and maze[x + (dx // 2)][y] == 0 and (x + dx, y) not in visit:
                visit.add((x + dx, y))
                q.append((x + dx, y, step + 1))
        for i in range(4):
            dx = dir[i][0]
            dy = dir[i][1]
            if maze[x + dx][y + dy] == 0 and (x + dx, y + dy) not in visit:
                visit.add((x + dx, y + dy))
                q.append((x + dx, y + dy, step + 1))
    return -1


res = BFS(2, 2)
print(res)
#直接原地修改maze
from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 2), (0, -2), (2, 0), (-2, 0)]
n, m = map(int, input().split())
maze = [[1 for _ in range(m + 4)] for _ in range(n + 4)]
for i in range(2, n + 2):
    maze[i][2:-2] = list(map(int, input().split()))


def BFS(x, y):
    q = deque([(x, y, 0)])

    while q:
        x, y, step = q.popleft()
        if x == n + 1 and y == m + 1:
            return step
        for i in range(4, 6):
            dy = dir[i][1]
            if maze[x][y + dy] == 0 and maze[x][y + (dy // 2)] == 0:
                maze[x][y + dy] = 1
                q.append((x, y + dy, step + 1))
        for i in range(6, 8):
            dx = dir[i][0]
            if maze[x + dx][y] == 0 and maze[x + (dx // 2)][y] == 0:
                maze[x + dx][y] = 1
                q.append((x + dx, y, step + 1))
        for i in range(4):
            dx = dir[i][0]
            dy = dir[i][1]
            if maze[x + dx][y + dy] == 0:
                maze[x + dx][y + dy] = 1
                q.append((x + dx, y + dy, step + 1))
    return -1


res = BFS(2, 2)
print(res)