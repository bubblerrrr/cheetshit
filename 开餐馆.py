def max_profit(n, k, m, p):
    # dp[i]表示到第i个位置的最大总利润
    # 由于m之间的距离断断续续，间隔较大，用索引表示。
    dp = p[:]
    for i in range(n):
        for j in range(i):
            if m[i] - m[j] > k:
                dp[i] = max(dp[i], dp[j] + p[i])
    return max(dp)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    p = list(map(int, input().split()))

    print(max_profit(n, k, m, p))