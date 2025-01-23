from collections import deque
n, m = map(int, input().split())
S=[]
maze = [["*" for _ in range(m + 2)] for _ in range(n + 2)]
for i in range(1,n+1):
    a=input()
    for j in range(len(a)):
        if a[j]=="S":
            S.append([i,j+1])
        maze[i][j+1]=a[j]
dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def BFS(x, y):
    q = deque([(x, y, 0)])
    while q:
        x, y, step = q.popleft()

        for i in range(4):
            dx = dir[i][0]
            dy = dir[i][1]
            if maze[x + dx][y + dy] == ".":
                maze[x + dx][y + dy] = "*"
                q.append((x + dx, y + dy, step + 1))
            if maze[x + dx][y + dy] == "T":
                return step + 1
    return -1

a,b=S
res = BFS(a,b)
print(res)