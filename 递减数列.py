n = int(input())
a = list(map(int, input().split()))
result = []
count = 1



for i in range(0, len(a) - 1):
    if a[i] <= a[i + 1]:
        count += 1
        if i==len(a)-2:
            result.append(count)
    else:
        result.append(count)
        count = 1
if count==len(a):
    print(len(a))
else:
    print(max(result))