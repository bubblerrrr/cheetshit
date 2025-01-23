import math


def fast():
    N = int(input())
    if N == 0:
        return None

    possibilities = []
    T0 = float('inf')
    for _ in range(N):
        v, t = map(int, input().split())
        if t >= 0:
            current_T0 = t + 4.5 / v * 3600
            T0 = min(current_T0, T0)
    T0 = math.ceil(T0)

    if T0 == float('inf'):
        return None

    return T0


m = int(input())
for _ in range(m):
    res = fast()
    print(res)