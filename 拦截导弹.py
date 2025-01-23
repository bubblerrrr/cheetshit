k=int(input())
h = list(map(int, input().split()))
# 选择状态：定义dp[i]为当最后一个导弹为i时的拦截数量
# 初始化数组，至少拦截一个导弹
dp = [1] * (k+1)
for i in range(1,k+1):
    for j in range(1,i):
        if h[j-1] >= h[i-1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
