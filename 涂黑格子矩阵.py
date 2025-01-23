#定义一个函数，判断涂色后是否形成四个黑格子
def heigezi(row,col):
    o=juzhen[row][col]
    a=juzhen[row-1][col-1]
    b=juzhen[row-1][col]
    c=juzhen[row-1][col+1]
    d=juzhen[row][col-1]
    e=juzhen[row][col+1]
    f=juzhen[row+1][col-1]
    g=juzhen[row+1][col]
    h=juzhen[row+1][col+1]
    if a+b+d+o==4 or b+c+o+e==4 or d+o+f+g==4 or o+e+g+h==4:
        return False
    else:
        return True
n,m,k=map(int,input().split())
juzhen=[[0 for _ in range(m+2)] for _ in range(n+2)]
tuse=[]

for _ in range(k):
    i,j=map(int,input().split())
    tuse.append((i,j))
for i in range(k):
    juzhen[tuse[i][0]][tuse[i][1]]=1
    if heigezi(tuse[i][0],tuse[i][1]):
        continue
    else:
        print(i+1)
        break
else:
    print(0)