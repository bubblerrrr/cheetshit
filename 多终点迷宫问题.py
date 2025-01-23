from collections import deque
n,m=map(int,input().split())
maze=[[1 for _ in range(m+2)]for _ in range(n+2)]
for i in range(1,n+1):
    maze[i][1:-1]=list(map(int,input().split()))
dir=[(1,0),(-1,0),(0,-1),(0,1)]
result=[]
def BFS(x,y):
    q=deque([(x,y,0)])
    maze[x][y]=1
    result.append((x,y,0))
    while q:
        x,y,step=q.popleft()
        for i in range(4):
            dx = dir[i][0]
            dy = dir[i][1]
            if maze[x+dx][y+dy]==0:
                q.append((x+dx,y+dy,step+1))
                result.append((x+dx,y+dy,step+1))
                maze[x+dx][y+dy]=1
BFS(1,1)
res=[[-1 for _ in range(m)] for _ in range(n)]
for i in result:
    a,b,c=i
    res[a-1][b-1]=c
for o in res:
    print(*o)