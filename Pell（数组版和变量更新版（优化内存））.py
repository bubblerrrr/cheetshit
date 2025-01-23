# 内存占用较大，因为数组将每一个数都存储下来了
# 优化：因为我们最后只需要求最后一个值，可以采用一直更新两个变量的方法
def Pell(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] * 2 + dp[i - 2]
    return dp[n]


n = int(input())
for i in range(n):
    m = int(input())
    result = Pell(m)
    print(result)


# 优化代码，用两个变量一直更新
def super_Pell(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a = 1  # P(n-2)
    b = 2  # P(n-1)
    for _ in range(3, n + 1):
        c = b * 2 + a  # P(n)
        a = b
        b = c  # P(n)被更新为b
    return b


n = int(input())
for _ in range(n):
    m = int(input())
    print(super_Pell(m))n,w