from collections import deque
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
maze = [[1 for _ in range(m+2)] for _ in range(n+2)]
for i in range(1, n + 1):
    maze[i][1:-1] = list(map(int, input().split()))
result = []
def BFS(x, y):
    q = deque([(x, y,0)])
    visit = set()
    visit.add((x, y))
    while q:
        x,y,step= q.popleft()
        if x == n and y == m:
            return step
        for i in range(4):
            dx = dir[i][0]
            dy = dir[i][1]
            if not maze[x + dx][y + dy] and (x+dx,y+dy) not in visit:
                q.append((x + dx, y + dy, step + 1))
                visit.add((x + dx, y + dy))
    return -1
res=BFS(1,1)
print(res)