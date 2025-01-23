n, a, b, c = map(int, input().split())
# 因为绳子的数量不可能为负数，所以将不可达数据定义为-1
# 随着dp[n]从0开始不断往上推，当遍历到n时，n前面的情况其实已经遍历过了，
# 如果三个if条件都无法满足的话，-1的不可达状态就未发生改变
dp = [-1] * (n + 1)
# 以dp【0】为初始化数据状态，确定了底层数据情况
dp[0] = 0
# 从底层往上遍历
for i in range(n + 1):
    if i >= a and dp[i - a] != -1:
        dp[i] = max(dp[i - a] + 1, dp[i])
    if i >= b and dp[i - b] != -1:
        dp[i] = max(dp[i - b] + 1, dp[i])
    if i >= c and dp[i - c] != -1:
        dp[i] = max(dp[i - c] + 1, dp[i])

print(dp[n])
