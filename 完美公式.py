def perfect_format():
    n = int(input())
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i ** 3
    for a in range(2,n+1):
        for b in range(2, a):
            for c in range(b, a):
                for d in range(c,a):
                    if dp[b] + dp[c] + dp[d] == dp[a]:
                        print(f'Cube = {a}, Triple = ({b},{c},{d})')
perfect_format()