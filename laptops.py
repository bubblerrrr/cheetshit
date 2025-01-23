n = int(input())
laptops = [tuple(map(int, input().split())) for _ in range(n)]

# 根据价格升序排序，如果价格相同则按质量降序排序
sorted_laptops = sorted(laptops, key=lambda x: (x[0], -x[1]))#排序时想以元组的第一个元素为标准排序，当第一个元素相同时，以第二个元素为标准排序

happy_alex = False
for i in range(len(sorted_laptops) - 1):
    if sorted_laptops[i][0] < sorted_laptops[i + 1][0] and sorted_laptops[i][1] > sorted_laptops[i + 1][1]:
        happy_alex = True
        break

if happy_alex:
    print("Happy Alex")
else:
    print("Poor Alex")

#以上为AI做法（当电脑的价格或者质量的数值有可能相同时）

#以下为自己的代码
n = int(input())
all_p = []
all_q = []
for _ in range(n):
    price, quality = map(int, input().split())
    all_p.append(price)
    all_q.append(quality)

computers = [(a, b) for a, b in zip(all_p, all_q)]
computers.sort(key=lambda x: x[0])
for i in range(n - 1):
    if computers[i][1] > computers[i + 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
    #或许可以使用暴力枚举法
n = int(input())
all_p = []
all_q = []
for _ in range(n):
    price, quality = map(int, input().split())
    all_p.append(price)
    all_q.append(quality)

computers = [(a, b) for a, b in zip(all_p, all_q)]
# 用True和False来标记是否已经达到if条件语句
found = False
for i in computers:
    if found:
        break
    for m in computers:
        if m[0] > i[0] and m[1] < i[1]:
            print("Happy Alex")
            found = True
            break

if not found:
    print("Poor Alex")

#这种解法会超时