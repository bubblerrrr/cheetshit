def shuliang():
    n = int(input())
    # 创造一个字典来保留最初状态，利用奇偶来判断开锁状态
    dict1 = {i: 0 for i in range(1, n + 1)}
    for m in range(1, n + 1):
        for h in dict1.keys():
            if h % m == 0:
                dict1[h] += 1

    count = 0
    # 判断最后字典里面有多少值是奇数，即为牢房开锁的数量
    for j in dict1.values():
        if j % 2 != 0:
            count += 1
    print(count)


t = int(input())
for _ in range(t):
    shuliang()

