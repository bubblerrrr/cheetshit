from collections import deque
import sys
input=sys.stdin.read
def is_valid(x,y,m,n):
    return 0<=x<m and 0<=y<n
def BFS(x,y,height,m,n,h,water_height):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque([(x,y,height)])
    water_height[x][y]=height
    while q:
        x,y,height=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if is_valid(nx,ny,m,n) and h[nx][ny]<height:
                if water_height[nx][ny]<height:
                    water_height[nx][ny]=height
                    q.append((nx,ny,height))


def main():
    data = input().split()
    idx = 0
    k = int(data[idx])
    idx += 1
    results = []
    for _ in range(k):
        m, n = map(int, data[idx:idx + 2])
        idx += 2
        h = []
        for i in range(m):
            h.append(list(map(int, data[idx:idx + n])))
            idx += n
        water_height = [[0 for _ in range(n)] for _ in range(m)]
        i, j = map(int, data[idx:idx + 2])
        idx += 2
        i, j = i - 1, j - 1
        p = int(data[idx])
        idx += 1
        for _ in range(p):
            x, y = map(int, data[idx:idx + 2])
            idx += 2
            x, y = x - 1, y - 1
            if h[x][y] <= h[i][j]:
                continue
            BFS(x, y, h[x][y], m, n, h, water_height)
        results.append("Yes" if water_height[i][j] > 0 else "No")
    sys.stdout.write("\n".join(results) + "\n")


main()
