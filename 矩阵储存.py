n, m1, m2 = map(int, input().split())
M1 = [[0 for _ in range(n)] for _ in range(n)]
M2 = [[0 for _ in range(n)] for _ in range(n)]
M3 = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m1):
    i, j, z = map(int, input().split())
    M1[i][j] = z
for _ in range(m2):
    i, j, z = map(int, input().split())
    M2[i][j] = z

for i in range(n):
    for j in range(n):
        for k in range(n):
            M3[i][j] += M1[i][k] * M2[k][j]
for i in range(n):
    for j in range(n):
        w= M3[i][j]
        if w!=0:
            print(i,j,w)