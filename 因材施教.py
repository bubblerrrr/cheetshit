n,m=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
#转换为差值的形式，将哪几个人分到一起，哪个班的内部差异就是那几个班的和
chazhi=[]
for i in range(n-1):
    chazhi.append(r[i+1]-r[i])
chazhi.sort(reverse=True)
print(sum(chazhi[m-1:]))