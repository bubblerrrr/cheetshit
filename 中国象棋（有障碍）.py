dir=[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
from collections import deque
n,m,x,y=map(int,input().split())
k=int(input())
maze=[[0 for _ in range(m)]for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    maze[a-1][b-1]=1
result=[]
def BFS(x,y):
    q=deque([(x,y,0)])
    result.append((x,y,0))
    visit=set()
    visit.add((x,y))
    while q:
        x,y,step=q.popleft()
        for i in range(0,2):
            dx=dir[i][0]
            dy=dir[i][1]
            if 0<=x+dx<n and 0<=y+dy<m and (x+dx,y+dy) not in visit and maze[x][y+1]!=1 and maze[x+dx][y+dy]!=1:
                q.append((x+dx,y+dy,step+1))
                result.append((x+dx,y+dy,step+1))
                visit.add((x+dx,y+dy))
        for i in range(2,4):
            dx=dir[i][0]
            dy=dir[i][1]
            if 0<=x+dx<n and 0<=y+dy<m and (x+dx,y+dy) not in visit and maze[x][y-1]!=1 and maze[x+dx][y+dy]!=1:
                q.append((x+dx,y+dy,step+1))
                result.append((x+dx,y+dy,step+1))
                visit.add((x+dx,y+dy))
        #没copy完，以下和上面结构一样