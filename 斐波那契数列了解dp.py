# 用斐波那契数列了解dp（动态规划）
# 题目F（0）=0，F（1）=1
# F（n）=F（n-1）+F（n-2）

# 普通方法会多次计算
# eg.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 改进：将底层的数据用数组储存起来（创建一个数组，并把值先计算出来），直接调用防止多次计算
def super_fib(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input())
print(super_fib(n))