n = int(input())
a = 0
b = 0
c = 0
for _ in range(n):
    h = list(map(int, input().split()))
    a += h[0]
    b += h[1]
    c += h[2]

if a == b == c == 0:
    print("YES")
else:
    print("NO")