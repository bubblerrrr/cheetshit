dir=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
from collections import deque
n,m,x,y=map(int,input().split())
maze=[[0 for _ in range(m)]for _ in range(n)]
result=[]
def BFS(x,y):
    q=deque([(x,y,0)])
    result.append((x,y,0))
    maze[x][y]=1
    while q:
        x,y,step=q.popleft()
        for i in range(8):
            dx=dir[i][0]
            dy=dir[i][1]
            if 0<=x+dx<n and 0<=y+dy<m and maze[x+dx][y+dy]==0:
                q.append((x+dx,y+dy,step+1))
                result.append((x+dx,y+dy,step+1))
                maze[x+dx][y+dy]=1
BFS(x-1,y-1)
res=[[-1 for _ in range(m)]for _ in range(n)]
for i in result:
    a,b,c=i
    res[a][b]=c
for i in res:
    print(*i)