n, m = map(int, input().split())
for _ in range(n):
    miane = list(map(int, input().split()))
dp = [float('inf') for _ in range(m + 1)]
dp[0] = 0
for i in range(m + 1):
    for o in miane:
        if i>=o:
            dp[i] = min(dp[i], dp[i - o] + 1)
if dp[m]==float('inf'):
    print(-1)
else:
    print(dp[m])