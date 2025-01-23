# pylint:skip-file
from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def BFS(x, y, height):
    global juzhen
    q = deque([(x, y)])
    visit=set()
    visit.add((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = dir[i][0]
            dy = dir[i][1]
            if 0 <= x + dx < M and 0 <= y + dy < N and height > juzhen[x + dx][y + dy] and (x+dx,y+dy) not in visit:
                q.append((x + dx, y + dy))
                visit.add((x+dx,y+dy))
    return visit

def www(M, N):
    global juzhen
    # True表示淹没了
    juzhen = []
    for i in range(M):
        row = list(map(int, input().split()))
        juzhen.append(row)
    target_x, target_y = map(int, input().split())
    num = int(input())
    box = set()
    for i in range(num):
        a, b = map(int, input().split())
        height = juzhen[a - 1][b - 1]
        current=BFS(a - 1, b - 1, height)
        box.update(current)
    if (target_x-1,target_y-1) in box:
        print("Yes")
    else:
        print("No")


k = int(input())
for _ in range(k):
    M, N = map(int, input().split())
    www(M, N)