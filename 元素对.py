n = int(input())
A = list(map(int, input().split()))
K = int(input())
count = 0
for i in A:
    m = K - i
    if m in A:
        count += 1

result = count // 2
print(result)
