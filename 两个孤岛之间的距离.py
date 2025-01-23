from collections import deque
dir=[(1,0),(-1,0),(0,-1),(0,1)]
q=deque()
def DFS(x,y,n,col,map,dir,q):
    map[x][y]=2
    q.append((x,y,0))
    for i in range(4):
        dx=dir[i][0]
        dy=dir[i][1]
        if 0<=x+dx<n and 0<=y+dy<col and map[x+dx][y+dy]==1:
            DFS(x+dx,y+dy,n,col,map,dir,q)
    return
def BFS(n,col,map,dir,q):
    while q:
        x,y,distance=q.popleft()
        for i in range(4):
            dx=dir[i][0]
            dy=dir[i][1]
            if 0<=x+dx<n and 0<=y+dy<col and map[x+dx][y+dy]==0:
                map[x+dx][y+dy]=2
                q.append((x+dx,y+dy,distance+1))
            if 0<=x+dx<n  and 0<=y+dy<col and map[x+dx][y+dy]==1:
                print(distance)
                exit(0)
def main():
    n = int(input())
    map = []
    for _ in range(n):
        current = [int(i) for i in input()]
        col = len(current)
        map.append(current)
    for i in range(n):
        Flag=False
        for j in range(col):
            if map[i][j]==1:
                DFS(i,j,n,col,map,dir,q)
                Flag=True
                break
        if Flag:
            break
    BFS(n,col,map,dir,q)
main()