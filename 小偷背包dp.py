N, B = map(int, input().split())
price = list(map(int, input().split()))
weight = list(map(int, input().split()))
#创建一个数组记录承重为j的背包在前i个物品最多能装多少价值的东西
dp=[[0 for _ in range(B+1)] for _ in range(N)]
# dp[i][j]:前i个物品承重为j，能装取的最大价值
for i in range(N):
    for j in range(B + 1):
        if j < weight[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + price[i])
print(dp[N-1][B])