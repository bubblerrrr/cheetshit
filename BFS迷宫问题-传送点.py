from collections import deque
dir=[(1,0),(-1,0),(0,1),(0,-1)]
n,m=map(int,input().split())
chuansongdian=[]
maze=[[1 for _ in range(m+2)]for _ in range(n+2)]
for i in range(1,n+1):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]==2:
            chuansongdian.append((i,j+1))
        maze[i][j+1]=a[j]
def BFS(x,y):
    q=deque([(x,y,0)])
    while q:
        x,y,step=q.popleft()
        if x==n and y==m:
            return step
        if (x,y)==chuansongdian[0] and maze[chuansongdian[1][0]][chuansongdian[1][1]]==2:
            q.append((chuansongdian[1][0],chuansongdian[1][1],step))
            maze[chuansongdian[1][0]][chuansongdian[1][1]] =1
        elif (x,y)==chuansongdian[1] and maze[chuansongdian[0][0]][chuansongdian[0][1]]==2:
            q.append((chuansongdian[0][0],chuansongdian[0][1],step))
            maze[chuansongdian[0][0]][chuansongdian[0][1]] =1
        for i in range(4):
            dx=dir[i][0]
            dy=dir[i][1]
            if maze[x+dx][y+dy]!=1:
                q.append((x+dx,y+dy,step+1))
                maze[x+dx][y+dy]=1
    return -1
res=BFS(1,1)
print(res)