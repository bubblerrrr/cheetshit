# dp[i][j]表示使用了i个精灵球，剩余体力为j时最多捕获的小精灵数量
n, m, k = map(int, input().split())
dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][m] = 0
for _ in range(k):
    a, b = map(int, input().split())
    for i in range(n, a - 1, -1):
        for j in range(b, m + 1):
            if i - a >= 0 and j - b >= 0 and dp[i - a][j - b] != -1:
                dp[i][j] = max(dp[i][j], dp[i - a][j - b] + 1)
max_capture = 0
max_health = 0
for c in range(n + 1):
    for h in range(m + 1):
        if dp[c][h] > max_capture:
            max_capture = dp[c][h]
            max_health = h
        elif dp[c][h] == max_capture:
            max_health = max(max_health, h)
print(max_capture, max_health)
