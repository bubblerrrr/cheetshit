#pylint:skip-file
dir=[(1,0),(0.-1),(-1,0),(0,1)]
from collections import deque
def game(w, h):
    maze = [[0 for _ in range(w+2)] for _ in range(h+2)]
    for i in range(1,h+1):
        a = input()
        for j in range(len(a)):
            if a[j] == "X":
                maze[i][j+1] = 1
def BFS(x1, y1, x2, y2,w,h):
    global maze
    q = deque([(x1, y1, 0, -1)])
    visit = set()
    visit.add((x1,y1))
    while q:
        x, y, step, count = q.popleft()
        if x == x2 and y == y2:
            return step
        for i in range(4):
            dx = dir[i][0]
            dy = dir[i][1]
            if 0 <= x+dx <h+2  and 0 <= y+dy < w+2 and (maze[x + dx][y + dy] == 0 or (x+dx==x1 and y+dy==y2)) and (x + dx, y + dy) not in visit:
                visit.add((x+dx, y+dy))
                if i == count:
                    q.append((x+dx, y+dy, step, i))
                else:
                    q.append((x+dx, y+dy, step + 1, i))
    return -1
B = 0
while True:
    B += 1
    w, h = map(int, input().split())
    if w == h == 0:
        break
    print(f'Board #{B}')
    game(w, h)
    P = 0

    while True:
        y1,x1,y2,x2 = map(int, input().split())
        if x1 == y1 == x2 == y2 == 0:
            break
        P += 1
        res = BFS(x1 - 1, y1 - 1, x2 - 1, y2 - 1,w,h)
        if res == -1:
            print(f'Pair {P}: impossible.')
        else:
            print(f'Pair {P}: {res} segments.')