def www(a, x):
    result = []
    i = 0
    while i < len(a):
        current_line = [a[i]]
        if sum(current_line) % x != 0:
            result.append(current_line[:])
        k = i + 1
        while k < len(a):
            current_line.append(a[k])
            if sum(current_line) % x != 0:
                result.append(current_line[:])
                k += 1
            else:
                k += 1
                continue
        i += 1
    length = []
    for i in result:
        length.append(len(i))
    if result:
        print(max(length))
    else:
        print(-1)


nCase = int(input())
for _ in range(nCase):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    www(a, x)

#简便版（注意子数组的概念）
def www(a, x):
    if sum(a) % x != 0:
        print(len(a))
        return
    result = []
    Flag = False
    for i in range(len(a)):
        if a[i] % x != 0:
            result.append(len(a) - i - 1)
            Flag = True
            break
    for i in range(len(a) - 1, -1, -1):
        if a[i] % x != 0:
            result.append(i)
            Flag = True
            break

    if Flag:
        print(max(result))
    else:
        print(-1)


nCase = int(input())
for _ in range(nCase):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    www(a, x)