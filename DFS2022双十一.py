#处理好输入输出
n,m=map(int,input().split())
price=[]
youhui=[]
dp=[0]*(m+1)
result=float("inf")
for i in range(n):
    price.append(input().split())
for i in range(m):
    youhui.append(input().split())
def DFS(i,sum1):
    global result
    if i==n:
        manjian=(sum1//300)*50
        jian=0
        for o in range(1,m+1):
            current=0
            for j in youhui[o-1]:
                 a,b=map(int,j.split("-"))
                 if dp[o]>=a:
                     current=max(current,b)
            jian+=current
        result=min(result,sum1-jian-manjian)
        return
    for i1 in price[i]:
        a,b=map(int,i1.split(":"))
        dp[a]+=b
        DFS(i+1,sum1+b)
        dp[a]-=b
DFS(0,0)
print(result)