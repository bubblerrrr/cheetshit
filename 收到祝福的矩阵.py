import math


def is_valid(s):
    if int(s) == 0:
        return False
    root = math.isqrt(int(s))
    if root * root == int(s):
        return True
    else:
        return False


s = input()
dp = [False] * (len(s) + 1)
dp[0] = True
for i in range(1, len(s) + 1):
    for j in range(i):
        if dp[j] and is_valid(s[j:i]):
            dp[i] = True
            break
if dp[len(s)]:
    print("Yes")
else:
    print("No")
