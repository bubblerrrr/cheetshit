def flower(t,k):
    dp=[0]*(100000+1)
    dp[0]=1
    #共i朵花可以分成几种组合情况
    #根据最后一朵或一组花来将第i多花和数量少一点的花扯上关系
    for i in range(1,100001):
        if i>=k:
            dp[i]=(dp[i-1]+dp[i-k])%1000000007
        else:
            dp[i]=dp[i-1]
    pre=[0]*100001
    pre[0]=dp[0]
    for i in range(1,100001):
        pre[i]=(pre[i-1]+dp[i])%1000000007
    for _ in range(t):
        a,b=map(int,input().split())
        if a==0:
            res=pre[b]
        else:
            res=(pre[b]-pre[a-1])%1000000007
        print(res)
t,k=map(int,input().split())
flower(t,k)