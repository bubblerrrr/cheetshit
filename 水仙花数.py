a, b = map(int, input().split())
result = []
for i in range(a, b + 1):
    x = i // 100
    y = (i % 100) // 10
    z = i % 10
    if x ** 3 + y ** 3 + z ** 3 == i:
        result.append(i)

if result:
    h = ' '.join(map(str, result))
    print(h)
else:
    print("NO")